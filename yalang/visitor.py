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

    def __init__(self, value, typ):
        self.value = value
        self.typ = typ

    def __repr__(self):
        return '{}:{}'.format(self.value, self.typ)

    def is_number(self):
        return self.typ == self.Type.NUMBER


class Function(Expression):
    def __init__(self, ctx, args, body):
        self.ctx = ctx
        self.args = args
        self.body = body
        self.typ = self.Type.FUNCTION

    def call(self, call_ctx, name, scope, params):
        if len(params) != len(self.args):
            raise VisitorException(call_ctx, "{} requires {} args, {} given", name, len(self.args), len(params))
        for k, v in zip(self.args, params):
            scope[k] = v
        v = Visitor(scope, is_fn=True)
        for stmt in self.body:
            v.visit(stmt)
            if v.return_value is not None:
                return v.return_value


class Visitor(YalangVisitor):
    def __init__(self, scope, debug=False, is_fn=False):
        super().__init__()
        self.errs = []
        self.scope = scope
        self.debug = debug
        self.debug_info = []
        self.is_fn = is_fn
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
        f = Function(ctx, [arg.text for arg in ctx.args], ctx.stmts)
        if self.debug:
            self.debug_info.append(f)
        return f

    def visitFnCall(self, ctx:YalangParser.FnCallContext):
        ident = ctx.ID().getText()
        f = self.scope.get(ident, None)
        if f is None:
            raise VisitorException(ctx, "Undefined variable {}", ident)
        params = [self.visit(p) for p in ctx.params]
        r = f.call(ctx, ident, self.scope.copy(), params)
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
