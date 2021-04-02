from enum import Enum

from yalang.generated.YalangParser import YalangParser
from yalang.generated.YalangVisitor import YalangVisitor
from yalang.exceptions import VisitorException

class Scope(dict):
    pass


class Expression(object):
    class Type(Enum):
        NUMBER = 1
        STRING = 2
        FUNCTION = 3
        STREAM = 3

    def __init__(self, value, typ):
        self.value = value
        self.typ = typ

    def __repr__(self):
        return '{}:{}'.format(self.value, self.typ)

    def is_number(self):
        return self.typ == self.Type.NUMBER


class Function(Expression):
    def __init__(self, ctx, scope, ins, args, outs, body):
        self.ctx = ctx
        if len(set(ins) & set(outs)) > 0:
            raise VisitorException(ctx, "Name clash between input and output streams")
        self.scope = scope
        self.ins = {i: Stream(True) for i in ins}
        self.args = args
        self.outs = {o: Stream(False) for o in outs}
        self.body = body
        self.typ = self.Type.FUNCTION
        self.scope.update(self.ins)
        self.scope.update(self.outs)
        self.value = None

    def call(self, call_ctx, params):
        if len(params) != len(self.args):
            raise VisitorException(call_ctx, "function requires {} args, {} given", len(self.args), len(params))
        for k, v in zip(self.args, params):
            self.scope[k] = v
        v = Visitor(self.scope, fn=self)
        for stmt in self.body:
            v.visit(stmt)
            if v.return_value is not None:
                return v.return_value


# TODO: Do something more sophisticated.
class Stream(Expression):
    def __init__(self, io:bool):
        self.io = io
        self.typ = self.Type.STREAM
        self.elements = []
        self.value = None

    def is_in(self):
        return self.io

    def size(self):
        return len(self.elements)

    def read(self):
        return self.elements.pop()

    def write(self, e):
        return self.elements.insert(0, e)


class Visitor(YalangVisitor):
    def __init__(self, scope, debug=False, fn=None):
        super().__init__()
        self.errs = []
        self.scope = scope
        self.debug = debug
        self.debug_info = []
        self.fn = fn
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
        r = f.call(ctx, params)
        if self.debug:
            self.debug_info.append(r)
        return r

    def visitReturnStmt(self, ctx:YalangParser.ReturnStmtContext):
        if self.fn is None:
            raise VisitorException(ctx, "Return statement is allowed only in functions")
        e = self.visit(ctx.expression())
        self.return_value = e
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitFnGetStream(self, ctx:YalangParser.FnGetStreamContext):
        l = self.visit(ctx.left)
        if l.typ != Expression.Type.FUNCTION:
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
        if self.fn is None and s.is_in():
            raise VisitorException(ctx, "Cannot read from input to another function")
        if self.fn is not None and s in self.fn.outs.values():
            raise VisitorException(ctx, "Cannot read from output within function")
        if s.size() == 0:
            raise VisitorException(ctx, "Attempted read from empty stream")
        e = s.read()
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitStreamWrite(self, ctx:YalangParser.StreamWriteContext):
        s = self.visit(ctx.right)
        if s.typ != Expression.Type.STREAM:
            raise VisitorException(ctx, "Cannot write to {}", l.typ)
        if self.fn is None and not s.is_in():
            raise VisitorException(ctx, "Cannot write to output of another function")
        if self.fn is not None and s in self.fn.ins.values():
            raise VisitorException(ctx, "Cannot write to input within function")
        e = self.visit(ctx.left)
        if self.debug:
            self.debug_info.append(e)
        return s.write(e)
