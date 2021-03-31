# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YalangParser import YalangParser
else:
    from YalangParser import YalangParser

# This class defines a complete generic visitor for a parse tree produced by YalangParser.

class YalangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YalangParser#program.
    def visitProgram(self, ctx:YalangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#statement.
    def visitStatement(self, ctx:YalangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#mathHigh.
    def visitMathHigh(self, ctx:YalangParser.MathHighContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#identifier.
    def visitIdentifier(self, ctx:YalangParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#unaryMinus.
    def visitUnaryMinus(self, ctx:YalangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#mathLow.
    def visitMathLow(self, ctx:YalangParser.MathLowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#nested.
    def visitNested(self, ctx:YalangParser.NestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#numberLiteral.
    def visitNumberLiteral(self, ctx:YalangParser.NumberLiteralContext):
        return self.visitChildren(ctx)



del YalangParser