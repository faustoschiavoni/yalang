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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\2\3\2\3\3\3\3\3\3\5\3\31\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\4\5")
        buf.write("\4\'\n\4\3\4\3\4\3\4\3\4\3\4\6\4.\n\4\r\4\16\4/\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4:\n\4\f\4\16\4=\13\4\3\4")
        buf.write("\5\4@\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("L\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4T\n\4\f\4\16\4W\13\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\4\3\2")
        buf.write("\n\f\4\2\t\t\r\r\2j\2\17\3\2\2\2\4\30\3\2\2\2\6K\3\2\2")
        buf.write("\2\bX\3\2\2\2\n[\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2\16\20")
        buf.write("\3\2\2\2\17\f\3\2\2\2\20\21\3\2\2\2\21\17\3\2\2\2\21\22")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\31")
        buf.write("\5\6\4\2\26\31\5\b\5\2\27\31\5\n\6\2\30\25\3\2\2\2\30")
        buf.write("\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\b\4\1\2\33")
        buf.write("L\7\23\2\2\34L\7\24\2\2\35&\7\4\2\2\36\37\7\22\2\2\37")
        buf.write("!\7\5\2\2 \36\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2")
        buf.write("#%\3\2\2\2$\"\3\2\2\2%\'\7\22\2\2&\"\3\2\2\2&\'\3\2\2")
        buf.write("\2\'(\3\2\2\2()\7\6\2\2)-\7\7\2\2*+\5\4\3\2+,\7\3\2\2")
        buf.write(",.\3\2\2\2-*\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\62\7\b\2\2\62L\3\2\2\2\63L\7\22\2\2\64")
        buf.write("\65\7\22\2\2\65?\7\4\2\2\66\67\5\6\4\2\678\7\5\2\28:\3")
        buf.write("\2\2\29\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2")
        buf.write("\2\2=;\3\2\2\2>@\5\6\4\2?;\3\2\2\2?@\3\2\2\2@A\3\2\2\2")
        buf.write("AL\7\6\2\2BC\7\t\2\2CL\5\6\4\7DE\7\4\2\2EF\5\6\4\2FG\7")
        buf.write("\6\2\2GL\3\2\2\2HI\7\22\2\2IJ\7\16\2\2JL\5\6\4\3K\32\3")
        buf.write("\2\2\2K\34\3\2\2\2K\35\3\2\2\2K\63\3\2\2\2K\64\3\2\2\2")
        buf.write("KB\3\2\2\2KD\3\2\2\2KH\3\2\2\2LU\3\2\2\2MN\f\5\2\2NO\t")
        buf.write("\2\2\2OT\5\6\4\6PQ\f\4\2\2QR\t\3\2\2RT\5\6\4\5SM\3\2\2")
        buf.write("\2SP\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\7\3\2\2\2")
        buf.write("WU\3\2\2\2XY\7\17\2\2YZ\5\6\4\2Z\t\3\2\2\2[\\\7\20\2\2")
        buf.write("\\]\5\6\4\2]\13\3\2\2\2\f\21\30\"&/;?KSU")
        return buf.getvalue()


class YalangParser ( Parser ):

    grammarFileName = "Yalang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'{'", "'}'", 
                     "'-'", "'*'", "'/'", "'%'", "'+'", "'='", "'!'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ID", 
                      "NUMBER", "STRING" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_printStmt = 3
    RULE_returnStmt = 4

    ruleNames =  [ "program", "statement", "expression", "printStmt", "returnStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    WS=15
    ID=16
    NUMBER=17
    STRING=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YalangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.StatementContext)
            else:
                return self.getTypedRuleContext(YalangParser.StatementContext,i)


        def getRuleIndex(self):
            return YalangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = YalangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 11
                self.match(YalangParser.T__0)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__1) | (1 << YalangParser.T__6) | (1 << YalangParser.T__12) | (1 << YalangParser.T__13) | (1 << YalangParser.ID) | (1 << YalangParser.NUMBER) | (1 << YalangParser.STRING))) != 0)):
                    break

            self.state = 17
            self.match(YalangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(YalangParser.PrintStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(YalangParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return YalangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = YalangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YalangParser.T__1, YalangParser.T__6, YalangParser.ID, YalangParser.NUMBER, YalangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.expression(0)
                pass
            elif token in [YalangParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.printStmt()
                pass
            elif token in [YalangParser.T__13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return YalangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MathHighContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YalangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathHigh" ):
                listener.enterMathHigh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathHigh" ):
                listener.exitMathHigh(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathHigh" ):
                return visitor.visitMathHigh(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YalangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(YalangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YalangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class FnLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self._ID = None # Token
            self.args = list() # of Tokens
            self._statement = None # StatementContext
            self.stmts = list() # of StatementContexts
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(YalangParser.ID)
            else:
                return self.getToken(YalangParser.ID, i)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.StatementContext)
            else:
                return self.getTypedRuleContext(YalangParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnLiteral" ):
                listener.enterFnLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnLiteral" ):
                listener.exitFnLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnLiteral" ):
                return visitor.visitFnLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FnCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self._expression = None # ExpressionContext
            self.params = list() # of ExpressionContexts
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(YalangParser.ID, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YalangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnCall" ):
                listener.enterFnCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnCall" ):
                listener.exitFnCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnCall" ):
                return visitor.visitFnCall(self)
            else:
                return visitor.visitChildren(self)


    class MathLowContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YalangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(YalangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathLow" ):
                listener.enterMathLow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathLow" ):
                listener.exitMathLow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathLow" ):
                return visitor.visitMathLow(self)
            else:
                return visitor.visitChildren(self)


    class NestedContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested" ):
                listener.enterNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested" ):
                listener.exitNested(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested" ):
                return visitor.visitNested(self)
            else:
                return visitor.visitChildren(self)


    class NumberLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a YalangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(YalangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLiteral" ):
                listener.enterNumberLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLiteral" ):
                listener.exitNumberLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLiteral" ):
                return visitor.visitNumberLiteral(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = YalangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = YalangParser.NumberLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(YalangParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = YalangParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(YalangParser.STRING)
                pass

            elif la_ == 3:
                localctx = YalangParser.FnLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(YalangParser.T__1)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==YalangParser.ID:
                    self.state = 32
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 28
                            localctx._ID = self.match(YalangParser.ID)
                            localctx.args.append(localctx._ID)
                            self.state = 29
                            self.match(YalangParser.T__2) 
                        self.state = 34
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    self.state = 35
                    localctx._ID = self.match(YalangParser.ID)
                    localctx.args.append(localctx._ID)


                self.state = 38
                self.match(YalangParser.T__3)
                self.state = 39
                self.match(YalangParser.T__4)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 40
                    localctx._statement = self.statement()
                    localctx.stmts.append(localctx._statement)
                    self.state = 41
                    self.match(YalangParser.T__0)
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__1) | (1 << YalangParser.T__6) | (1 << YalangParser.T__12) | (1 << YalangParser.T__13) | (1 << YalangParser.ID) | (1 << YalangParser.NUMBER) | (1 << YalangParser.STRING))) != 0)):
                        break

                self.state = 47
                self.match(YalangParser.T__5)
                pass

            elif la_ == 4:
                localctx = YalangParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(YalangParser.ID)
                pass

            elif la_ == 5:
                localctx = YalangParser.FnCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(YalangParser.ID)
                self.state = 51
                self.match(YalangParser.T__1)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__1) | (1 << YalangParser.T__6) | (1 << YalangParser.ID) | (1 << YalangParser.NUMBER) | (1 << YalangParser.STRING))) != 0):
                    self.state = 57
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 52
                            localctx._expression = self.expression(0)
                            localctx.params.append(localctx._expression)
                            self.state = 53
                            self.match(YalangParser.T__2) 
                        self.state = 59
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                    self.state = 60
                    localctx._expression = self.expression(0)
                    localctx.params.append(localctx._expression)


                self.state = 63
                self.match(YalangParser.T__3)
                pass

            elif la_ == 6:
                localctx = YalangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(YalangParser.T__6)
                self.state = 65
                self.expression(5)
                pass

            elif la_ == 7:
                localctx = YalangParser.NestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(YalangParser.T__1)
                self.state = 67
                self.expression(0)
                self.state = 68
                self.match(YalangParser.T__3)
                pass

            elif la_ == 8:
                localctx = YalangParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(YalangParser.ID)
                self.state = 71
                self.match(YalangParser.T__11)
                self.state = 72
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = YalangParser.MathHighContext(self, YalangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__7) | (1 << YalangParser.T__8) | (1 << YalangParser.T__9))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = YalangParser.MathLowContext(self, YalangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==YalangParser.T__6 or _la==YalangParser.T__10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.right = self.expression(3)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return YalangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = YalangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(YalangParser.T__12)
            self.state = 87
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(YalangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return YalangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = YalangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(YalangParser.T__13)
            self.state = 90
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




