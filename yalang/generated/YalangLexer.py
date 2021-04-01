# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13")
        buf.write("\65\n\13\r\13\16\13\66\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\5\16A\n\16\3\16\3\16\3\16\7\16F\n\16\f\16\16\16")
        buf.write("I\13\16\3\17\6\17L\n\17\r\17\16\17M\3\17\3\17\6\17R\n")
        buf.write("\17\r\17\16\17S\5\17V\n\17\3\20\3\20\7\20Z\n\20\f\20\16")
        buf.write("\20]\13\20\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16\37\17\3\2\5\5")
        buf.write("\2\13\f\17\17\"\"\4\2C\\c|\5\2\f\f\17\17))\2f\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!")
        buf.write("\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2")
        buf.write("\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\64")
        buf.write("\3\2\2\2\27:\3\2\2\2\31<\3\2\2\2\33@\3\2\2\2\35K\3\2\2")
        buf.write("\2\37W\3\2\2\2!\"\7=\2\2\"\4\3\2\2\2#$\7?\2\2$\6\3\2\2")
        buf.write("\2%&\7/\2\2&\b\3\2\2\2\'(\7*\2\2(\n\3\2\2\2)*\7+\2\2*")
        buf.write("\f\3\2\2\2+,\7,\2\2,\16\3\2\2\2-.\7\61\2\2.\20\3\2\2\2")
        buf.write("/\60\7\'\2\2\60\22\3\2\2\2\61\62\7-\2\2\62\24\3\2\2\2")
        buf.write("\63\65\t\2\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2")
        buf.write("\2\66\67\3\2\2\2\678\3\2\2\289\b\13\2\29\26\3\2\2\2:;")
        buf.write("\4\62;\2;\30\3\2\2\2<=\t\3\2\2=\32\3\2\2\2>A\5\31\r\2")
        buf.write("?A\7a\2\2@>\3\2\2\2@?\3\2\2\2AG\3\2\2\2BF\5\31\r\2CF\5")
        buf.write("\27\f\2DF\7a\2\2EB\3\2\2\2EC\3\2\2\2ED\3\2\2\2FI\3\2\2")
        buf.write("\2GE\3\2\2\2GH\3\2\2\2H\34\3\2\2\2IG\3\2\2\2JL\5\27\f")
        buf.write("\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NU\3\2\2\2O")
        buf.write("Q\7\60\2\2PR\5\27\f\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST")
        buf.write("\3\2\2\2TV\3\2\2\2UO\3\2\2\2UV\3\2\2\2V\36\3\2\2\2W[\7")
        buf.write(")\2\2XZ\n\4\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2")
        buf.write("\2\\^\3\2\2\2][\3\2\2\2^_\7)\2\2_ \3\2\2\2\13\2\66@EG")
        buf.write("MSU[\3\b\2\2")
        return buf.getvalue()


class YalangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    WS = 10
    ID = 11
    NUMBER = 12
    STRING = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'-'", "'('", "')'", "'*'", "'/'", "'%'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "NUMBER", "STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "WS", "DIGIT", "LETTER", "ID", "NUMBER", 
                  "STRING" ]

    grammarFileName = "Yalang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


