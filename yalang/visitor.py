from enum import Enum

from gevent import Greenlet
from gevent.hub import get_hub
from gevent.queue import Queue
from gevent.exceptions import LoopExit

from yalang.generated.YalangParser import YalangParser
from yalang.generated.YalangVisitor import YalangVisitor
from yalang.exceptions import VisitorException

# Do not dump greenlet traces
get_hub().exception_stream = None

class Scope(dict):
    pass


class Expression(object):
    class Type(Enum):
        VOID = -2
        EOS = -1
        NUMBER = 1
        STRING = 2
        FUNCTION = 3
        STREAM = 4
        ASYNC_CALL = 5

    def __init__(self, value, typ):
        self.value = value
        self.typ = typ

    def __repr__(self):
        return '{}:{}'.format(self.value, self.typ)

    def is_number(self):
        return self.typ == self.Type.NUMBER


# Use for determining if a stream has been closed.
EOS = Expression(None, Expression.Type.EOS)
VOID = Expression(None, Expression.Type.VOID)


def call_fn(scope, body, async_fn=None, async_calls=None):
    v = Visitor(scope, is_fn=True, async_fn=async_fn, async_calls=async_calls)
    for stmt in body:
        v.visit(stmt)
        if v.return_value is not None:
            return v.return_value
    return VOID


class Function(Expression):
    def __init__(self, ctx, scope, ins, args, outs, body):
        self.ctx = ctx
        if len(set(ins) & set(outs)) > 0:
            raise VisitorException(ctx, "Name clash between input and output streams")
        self.scope = scope
        self.ins = ins
        self.args = args
        self.outs = outs
        self.is_async = len(ins) > 0 or len(outs) > 0
        self.body = body
        self.exception = None
        self.typ = self.Type.FUNCTION
        self.value = None


    def call(self, call_ctx, params, async_calls):
        if len(params) != len(self.args):
            raise VisitorException(call_ctx, "function requires {} args, {} given", len(self.args), len(params))

        scope = self.scope.copy()
        for k, v in zip(self.args, params):
            scope[k] = v

        if self.is_async:
            ac = AsyncCall(scope, self.ins, self.outs, self.body)
            ac.start(async_calls)
            return ac
        else:
            return call_fn(scope, self.body, async_calls=async_calls)


class Stream(Expression):
    def __init__(self, io:bool):
        self.io = io
        self.typ = self.Type.STREAM
        self.q = Queue()
        self.closed = False
        self.value = None

    def is_in(self):
        return self.io

    def read(self):
        if self.closed:
            return None
        e = self.q.get()
        if e == EOS:
            self.closed = True
            return None
        return e

    def write(self, e):
        return self.q.put(e)


class AsyncCall(Expression):
    def __init__(self, scope, ins, outs, body):
        self.scope = scope
        self.body = body
        self.ins = {i: Stream(True) for i in ins}
        self.outs = {o: Stream(False) for o in outs}
        self.scope.update(self.ins)
        self.scope.update(self.outs)
        self.typ = self.Type.ASYNC_CALL
        self.value = None

    def start(self, async_calls):
        self.g = Greenlet.spawn(call_fn, self.scope, self.body, async_fn=self, async_calls=async_calls)
        async_calls.append(self)

        # def exception_callback(glet):
        #     raise glet.exception
        #
        # self.g.link_exception(exception_callback)
        return self.g

    def wait(self):
        return self.g.get()


class Visitor(YalangVisitor):
    def __init__(self, scope, debug=False, is_fn=False, async_fn=None, async_calls=None):
        super().__init__()
        self.errs = []
        self.async_calls = async_calls
        if self.async_calls is None:
            self.async_calls = []
        self.scope = scope
        self.debug = debug
        self.debug_info = []
        self.async_fn = async_fn
        self.is_fn = is_fn or self.async_fn is not None
        self.is_main = not self.is_fn
        self.return_value = None

    def checkErrors(self):
        return len(self.errs) > 0

    # def defaultResult(self):
    #     return Expression('')
    #
    # def aggregateResult(self, agg, res):
    #     return Expression(agg.value + res.value, agg.err or res.err)

    def visitErrorNode(self, errNode):
        self.errs.append(errNode)


    def visitProgram(self, ctx:YalangParser.ProgramContext):
        r = self.visitChildren(ctx)
        if self.is_main:
            for ac in self.async_calls:
                ac.wait()
        return r

    def visitUnaryMinus(self, ctx:YalangParser.UnaryMinusContext):
        expr = self.visit(ctx.expression())
        if not expr.is_number():
            raise VisitorException(ctx, "Unary Math on non-numeric value: -{}", expr)
        e = Expression('-' + expr.value, expr.typ)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitBinaryMath(self, ctx):
        op = ctx.op.text
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        if not l.is_number() or not r.is_number():
            raise VisitorException(ctx, "Binary Math on non-numeric values: {} {} {}", l.value, op, r.value)
        r = eval(l.value + op + r.value)
        e = Expression(str(r), l.typ)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitMathHigh(self, ctx:YalangParser.MathHighContext):
        return self.visitBinaryMath(ctx)

    def visitMathLow(self, ctx:YalangParser.MathLowContext):
        return self.visitBinaryMath(ctx)

    def visitNumberLiteral(self, ctx:YalangParser.NumberLiteralContext):
        e = Expression(ctx.NUMBER().getText(), Expression.Type.NUMBER)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitStringLiteral(self, ctx:YalangParser.StringLiteralContext):
        e = Expression(ctx.STRING().getText(), Expression.Type.STRING)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitNested(self, ctx:YalangParser.NestedContext):
        e = self.visit(ctx.expression())
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitAssignment(self, ctx:YalangParser.AssignmentContext):
        e = self.visit(ctx.expression())
        ident = ctx.ID().getText()
        self.scope[ident] = e
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitIdentifier(self, ctx:YalangParser.IdentifierContext):
        ident = ctx.ID().getText()
        e = self.scope.get(ident, None)
        if e is None:
            raise VisitorException(ctx, "Undefined variable {}", ident)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitPrintStmt(self, ctx:YalangParser.PrintStmtContext):
        e = self.visit(ctx.expression())
        print(e.value)

    def visitFnLiteral(self, ctx:YalangParser.FnLiteralContext):
        f = Function(
            ctx,
            self.scope.copy(),
            [i.text for i in ctx.ins],
            [arg.text for arg in ctx.args],
            [o.text for o in ctx.outs],
            ctx.stmts
        )
        if self.debug:
            self.debug_info.append(f)
        return f

    def visitFnCall(self, ctx:YalangParser.FnCallContext):
        f = self.visit(ctx.callee)
        if f.typ != Expression.Type.FUNCTION:
            raise VisitorException(ctx, "variable is not callable")
        params = [self.visit(p) for p in ctx.params]
        r = f.call(ctx, params, self.async_calls)
        if self.debug:
            self.debug_info.append(r)
        return r

    def visitReturnStmt(self, ctx:YalangParser.ReturnStmtContext):
        if not self.is_fn:
            raise VisitorException(ctx, "Return statement is allowed only in functions")
        e = self.visit(ctx.expression())
        self.return_value = e
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitFnGetStream(self, ctx:YalangParser.FnGetStreamContext):
        l = self.visit(ctx.left)
        if l.typ != Expression.Type.ASYNC_CALL:
            raise VisitorException(ctx, "Cannot get stream from {}", l.typ)
        ident = ctx.right.text
        s = l.ins.get(ident, None)
        if s is None:
            s = l.outs.get(ident, None)
        if s is None:
            raise VisitorException(ctx, "Cannot get stream {}", ident)
        if self.debug:
            self.debug_info.append(s)
        return s

    def visitStreamRead(self, ctx:YalangParser.StreamReadContext):
        s = self.visit(ctx.expression())
        if s.typ != Expression.Type.STREAM:
            raise VisitorException(ctx, "Cannot read from {}", l.typ)
        if self.async_fn is None and s.is_in():
            raise VisitorException(ctx, "Cannot read from input to another function")
        if self.async_fn is not None and s in self.async_fn.outs.values():
            raise VisitorException(ctx, "Cannot read from output within function")
        try:
            e = s.read()
        except LoopExit as ex:
            raise VisitorException(ctx, "Deadlock detected")
        if e is None:
            raise VisitorException(ctx, "Attempted read from empty stream")
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitStreamWrite(self, ctx:YalangParser.StreamWriteContext):
        s = self.visit(ctx.right)
        if s.typ != Expression.Type.STREAM:
            raise VisitorException(ctx, "Cannot write to {}", l.typ)
        if self.async_fn is None and not s.is_in():
            raise VisitorException(ctx, "Cannot write to output of another function")
        if self.async_fn is not None and s in self.async_fn.ins.values():
            raise VisitorException(ctx, "Cannot write to input within function")
        e = self.visit(ctx.left)
        if self.debug:
            self.debug_info.append(e)
        return s.write(e)

    def visitCloseStmt(self, ctx:YalangParser.CloseStmtContext):
        s = self.visit(ctx.stream)
        if s.typ != Expression.Type.STREAM:
            raise VisitorException(ctx, "Cannot close {}", s.typ)
        s.write(EOS)
