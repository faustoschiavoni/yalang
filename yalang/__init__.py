from antlr4 import *

from yalang.exceptions import YalangException
from yalang.generated.YalangLexer import YalangLexer
from yalang.generated.YalangParser import YalangParser
from yalang.visitor import Visitor, Scope

def execute_string(text, scope=Scope(), debug=False):
    lexer = YalangLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = YalangParser(stream)
    program = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        # TODO: use error listeners when parsing:
        # https://www.antlr.org/api/Java/org/antlr/v4/runtime/Recognizer.html#addErrorListener(org.antlr.v4.runtime.ANTLRErrorListener)
        raise YalangException("Syntax errors...")

    visitor = Visitor(scope, debug=debug)
    visitor.visit(program)
    return visitor

def execute_file(file):
    with open(file, 'r') as fp:
        return execute_string(fp.read())
