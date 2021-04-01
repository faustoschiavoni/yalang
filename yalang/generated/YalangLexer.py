# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\6\f9\n\f\r\f\16\f:\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\5\17E\n\17\3\17\3\17\3\17\7\17J\n\17\f")
        buf.write("\17\16\17M\13\17\3\20\6\20P\n\20\r\20\16\20Q\3\20\3\20")
        buf.write("\6\20V\n\20\r\20\16\20W\5\20Z\n\20\3\21\3\21\7\21^\n\21")
        buf.write("\f\21\16\21a\13\21\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17")
        buf.write("!\20\3\2\5\5\2\13\f\17\17\"\"\4\2C\\c|\5\2\f\f\17\17)")
        buf.write(")\2j\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t")
        buf.write(")\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2")
        buf.write("\2\2\23\63\3\2\2\2\25\65\3\2\2\2\278\3\2\2\2\31>\3\2\2")
        buf.write("\2\33@\3\2\2\2\35D\3\2\2\2\37O\3\2\2\2![\3\2\2\2#$\7=")
        buf.write("\2\2$\4\3\2\2\2%&\7?\2\2&\6\3\2\2\2\'(\7/\2\2(\b\3\2\2")
        buf.write("\2)*\7*\2\2*\n\3\2\2\2+,\7+\2\2,\f\3\2\2\2-.\7,\2\2.\16")
        buf.write("\3\2\2\2/\60\7\61\2\2\60\20\3\2\2\2\61\62\7\'\2\2\62\22")
        buf.write("\3\2\2\2\63\64\7-\2\2\64\24\3\2\2\2\65\66\7#\2\2\66\26")
        buf.write("\3\2\2\2\679\t\2\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:")
        buf.write(";\3\2\2\2;<\3\2\2\2<=\b\f\2\2=\30\3\2\2\2>?\4\62;\2?\32")
        buf.write("\3\2\2\2@A\t\3\2\2A\34\3\2\2\2BE\5\33\16\2CE\7a\2\2DB")
        buf.write("\3\2\2\2DC\3\2\2\2EK\3\2\2\2FJ\5\33\16\2GJ\5\31\r\2HJ")
        buf.write("\7a\2\2IF\3\2\2\2IG\3\2\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2")
        buf.write("\2\2KL\3\2\2\2L\36\3\2\2\2MK\3\2\2\2NP\5\31\r\2ON\3\2")
        buf.write("\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RY\3\2\2\2SU\7\60\2")
        buf.write("\2TV\5\31\r\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2")
        buf.write("XZ\3\2\2\2YS\3\2\2\2YZ\3\2\2\2Z \3\2\2\2[_\7)\2\2\\^\n")
        buf.write("\4\2\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2")
        buf.write("\2\2a_\3\2\2\2bc\7)\2\2c\"\3\2\2\2\13\2:DIKQWY_\3\b\2")
        buf.write("\2")
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
    T__9 = 10
    WS = 11
    ID = 12
    NUMBER = 13
    STRING = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'-'", "'('", "')'", "'*'", "'/'", "'%'", "'+'", 
            "'!'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ID", "NUMBER", "STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS", "DIGIT", "LETTER", "ID", 
                  "NUMBER", "STRING" ]

    grammarFileName = "Yalang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


