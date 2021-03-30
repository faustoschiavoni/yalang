from yalang.generated.YalangParser import YalangParser
from yalang.generated.YalangVisitor import YalangVisitor


class Expression(object):
    def __init__(self, value, err=False):
        self.value = value
        self.err = err

    def __repr__(self):
        if self.err:
            return 'ERROR: {}'.format(self.value)
        return '{}'.format(self.value)


class Visitor(YalangVisitor):
    def defaultResult(self):
        return Expression('')

    def visitErrorNode(self, errNode):
        return Expression('', True)

    def aggregateResult(self, agg, res):
        return Expression(agg.value + res.value, agg.err or res.err)

    def visitHi(self, ctx:YalangParser.HiContext):
        return Expression(str(ctx.ID()))
