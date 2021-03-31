from yalang.generated.YalangParser import YalangParser
from yalang.generated.YalangVisitor import YalangVisitor
from yalang.exceptions import YalangException

class Scope(dict):
    pass

class Expression(object):
    def __init__(self, value, err=False):
        self.value = value
        self.err = err

    def __repr__(self):
        if self.err:
            return 'ERROR: {}'.format(self.value)
        return '{}'.format(self.value)


class Visitor(YalangVisitor):
    def __init__(self, scope, debug=False):
        super().__init__()
        self.errs = []
        self.scope = scope
        self.debug = debug
        self.debug_info = []

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
        if not expr.value.isnumeric():
            raise Exception("Unary Math on non-numeric value: -{}", expr)
        e = Expression('-' + expr.value)
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitBinaryMath(self, left, op, right):
        l = self.visit(left)
        r = self.visit(right)
        ls = l.value
        if ls[0] == '-':
            ls = ls[1:]
        rs = r.value
        if rs[0] == '-':
            rs = rs[1:]
        if not ls.isnumeric() or not rs.isnumeric():
            raise YalangException("Binary Math on non-numeric values: {} {} {}".format(l, op, r))
        r = eval(l.value + op + r.value)
        e = Expression(str(r))
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitMathHigh(self, ctx:YalangParser.MathHighContext):
        return self.visitBinaryMath(ctx.left, ctx.op.text, ctx.right)

    def visitMathLow(self, ctx:YalangParser.MathLowContext):
        return self.visitBinaryMath(ctx.left, ctx.op.text, ctx.right)

    def visitNumberLiteral(self, ctx:YalangParser.NumberLiteralContext):
        e = Expression(ctx.NUMBER().getText())
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitNested(self, ctx:YalangParser.NestedContext):
        e = self.visit(ctx.expression())
        if self.debug:
            self.debug_info.append(e)
        return e

    def visitIdentifier(self, ctx:YalangParser.IdentifierContext):
        e = Expression(ctx.ID().getText())
        if self.debug:
            self.debug_info.append(e)
        return e
