# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YalangParser import YalangParser
else:
    from YalangParser import YalangParser

# This class defines a complete generic visitor for a parse tree produced by YalangParser.

class YalangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YalangParser#prog.
    def visitProg(self, ctx:YalangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YalangParser#hi.
    def visitHi(self, ctx:YalangParser.HiContext):
        return self.visitChildren(ctx)



del YalangParser
