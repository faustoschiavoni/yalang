# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\6\n/\n\n\r\n\16\n\60\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\5\r;\n\r\3\r\3\r\3\r\7\r@\n\r\f")
        buf.write("\r\16\rC\13\r\3\16\6\16F\n\16\r\16\16\16G\3\16\3\16\6")
        buf.write("\16L\n\16\r\16\16\16M\5\16P\n\16\2\2\17\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33\r\3\2\4")
        buf.write("\5\2\13\f\17\17\"\"\4\2C\\c|\2V\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2")
        buf.write("\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23")
        buf.write(".\3\2\2\2\25\64\3\2\2\2\27\66\3\2\2\2\31:\3\2\2\2\33E")
        buf.write("\3\2\2\2\35\36\7=\2\2\36\4\3\2\2\2\37 \7/\2\2 \6\3\2\2")
        buf.write("\2!\"\7*\2\2\"\b\3\2\2\2#$\7+\2\2$\n\3\2\2\2%&\7,\2\2")
        buf.write("&\f\3\2\2\2\'(\7\61\2\2(\16\3\2\2\2)*\7\'\2\2*\20\3\2")
        buf.write("\2\2+,\7-\2\2,\22\3\2\2\2-/\t\2\2\2.-\3\2\2\2/\60\3\2")
        buf.write("\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\b\n")
        buf.write("\2\2\63\24\3\2\2\2\64\65\4\62;\2\65\26\3\2\2\2\66\67\t")
        buf.write("\3\2\2\67\30\3\2\2\28;\5\27\f\29;\7a\2\2:8\3\2\2\2:9\3")
        buf.write("\2\2\2;A\3\2\2\2<@\5\27\f\2=@\5\25\13\2>@\7a\2\2?<\3\2")
        buf.write("\2\2?=\3\2\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2")
        buf.write("B\32\3\2\2\2CA\3\2\2\2DF\5\25\13\2ED\3\2\2\2FG\3\2\2\2")
        buf.write("GE\3\2\2\2GH\3\2\2\2HO\3\2\2\2IK\7\60\2\2JL\5\25\13\2")
        buf.write("KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OI\3")
        buf.write("\2\2\2OP\3\2\2\2P\34\3\2\2\2\n\2\60:?AGMO\3\b\2\2")
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
    WS = 9
    ID = 10
    NUMBER = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'-'", "'('", "')'", "'*'", "'/'", "'%'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "NUMBER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "WS", "DIGIT", "LETTER", "ID", "NUMBER" ]

    grammarFileName = "Yalang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


