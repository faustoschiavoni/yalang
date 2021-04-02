from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from yalang.exceptions import ParseException, YalangException
from yalang.generated.YalangLexer import YalangLexer
from yalang.generated.YalangParser import YalangParser
from yalang.visitor import Visitor, Scope

class ParserErrorListener(ErrorListener):
    def __init__(self):
        self.errs = []

    def syntaxError(self, recognizer, symbol, line:int, column:int, msg:str, e):
        self.errs.append("line " + str(line) + ":" + str(column) + " " + msg)


def execute_string(text, scope=None, debug=False):
    lexer = YalangLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    errs = ParserErrorListener()
    parser = YalangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(errs)
    program = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise ParseException('\n'.join(errs.errs))
    if scope is None:
        scope = Scope()
    visitor = Visitor(scope, debug=debug)
    visitor.visit(program)
    return visitor

def execute_file(file):
    with open(file, 'r') as fp:
        return execute_string(fp.read())
