# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YalangParser import YalangParser
else:
    from YalangParser import YalangParser

# This class defines a complete listener for a parse tree produced by YalangParser.
class YalangListener(ParseTreeListener):

    # Enter a parse tree produced by YalangParser#program.
    def enterProgram(self, ctx:YalangParser.ProgramContext):
        pass

    # Exit a parse tree produced by YalangParser#program.
    def exitProgram(self, ctx:YalangParser.ProgramContext):
        pass


    # Enter a parse tree produced by YalangParser#statement.
    def enterStatement(self, ctx:YalangParser.StatementContext):
        pass

    # Exit a parse tree produced by YalangParser#statement.
    def exitStatement(self, ctx:YalangParser.StatementContext):
        pass


    # Enter a parse tree produced by YalangParser#mathHigh.
    def enterMathHigh(self, ctx:YalangParser.MathHighContext):
        pass

    # Exit a parse tree produced by YalangParser#mathHigh.
    def exitMathHigh(self, ctx:YalangParser.MathHighContext):
        pass


    # Enter a parse tree produced by YalangParser#identifier.
    def enterIdentifier(self, ctx:YalangParser.IdentifierContext):
        pass

    # Exit a parse tree produced by YalangParser#identifier.
    def exitIdentifier(self, ctx:YalangParser.IdentifierContext):
        pass


    # Enter a parse tree produced by YalangParser#stringLiteral.
    def enterStringLiteral(self, ctx:YalangParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by YalangParser#stringLiteral.
    def exitStringLiteral(self, ctx:YalangParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by YalangParser#assignment.
    def enterAssignment(self, ctx:YalangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YalangParser#assignment.
    def exitAssignment(self, ctx:YalangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YalangParser#unaryMinus.
    def enterUnaryMinus(self, ctx:YalangParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by YalangParser#unaryMinus.
    def exitUnaryMinus(self, ctx:YalangParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by YalangParser#mathLow.
    def enterMathLow(self, ctx:YalangParser.MathLowContext):
        pass

    # Exit a parse tree produced by YalangParser#mathLow.
    def exitMathLow(self, ctx:YalangParser.MathLowContext):
        pass


    # Enter a parse tree produced by YalangParser#nested.
    def enterNested(self, ctx:YalangParser.NestedContext):
        pass

    # Exit a parse tree produced by YalangParser#nested.
    def exitNested(self, ctx:YalangParser.NestedContext):
        pass


    # Enter a parse tree produced by YalangParser#numberLiteral.
    def enterNumberLiteral(self, ctx:YalangParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by YalangParser#numberLiteral.
    def exitNumberLiteral(self, ctx:YalangParser.NumberLiteralContext):
        pass



del YalangParser