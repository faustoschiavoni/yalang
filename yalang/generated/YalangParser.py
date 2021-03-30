# Generated from /home/affo/coding/yalang/yalang/Yalang.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\22\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\20\2\t\3\2\2\2\4")
        buf.write("\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2\t\7\3")
        buf.write("\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r\7\2\2")
        buf.write("\3\r\3\3\2\2\2\16\17\7\3\2\2\17\20\7\4\2\2\20\5\3\2\2")
        buf.write("\2\3\t")
        return buf.getvalue()


class YalangParser ( Parser ):

    grammarFileName = "Yalang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_prog = 0
    RULE_hi = 1

    ruleNames =  [ "prog", "hi" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YalangParser.EOF, 0)

        def hi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.HiContext)
            else:
                return self.getTypedRuleContext(YalangParser.HiContext,i)


        def getRuleIndex(self):
            return YalangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = YalangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==YalangParser.T__0:
                self.state = 4
                self.hi()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(YalangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(YalangParser.ID, 0)

        def getRuleIndex(self):
            return YalangParser.RULE_hi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHi" ):
                listener.enterHi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHi" ):
                listener.exitHi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHi" ):
                return visitor.visitHi(self)
            else:
                return visitor.visitChildren(self)




    def hi(self):

        localctx = YalangParser.HiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(YalangParser.T__0)
            self.state = 13
            self.match(YalangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





