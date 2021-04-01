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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\2\3\2\3\3\3\3\5\3\26\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4%\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\5\3")
        buf.write("\5\3\5\3\5\2\3\6\6\2\4\6\b\2\4\3\2\b\n\4\2\5\5\13\13\2")
        buf.write("9\2\r\3\2\2\2\4\25\3\2\2\2\6$\3\2\2\2\b\61\3\2\2\2\n\13")
        buf.write("\5\4\3\2\13\f\7\3\2\2\f\16\3\2\2\2\r\n\3\2\2\2\16\17\3")
        buf.write("\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21\22")
        buf.write("\7\2\2\3\22\3\3\2\2\2\23\26\5\6\4\2\24\26\5\b\5\2\25\23")
        buf.write("\3\2\2\2\25\24\3\2\2\2\26\5\3\2\2\2\27\30\b\4\1\2\30%")
        buf.write("\7\17\2\2\31%\7\20\2\2\32%\7\16\2\2\33\34\7\16\2\2\34")
        buf.write("\35\7\4\2\2\35%\5\6\4\7\36\37\7\5\2\2\37%\5\6\4\6 !\7")
        buf.write("\6\2\2!\"\5\6\4\2\"#\7\7\2\2#%\3\2\2\2$\27\3\2\2\2$\31")
        buf.write("\3\2\2\2$\32\3\2\2\2$\33\3\2\2\2$\36\3\2\2\2$ \3\2\2\2")
        buf.write("%.\3\2\2\2&\'\f\4\2\2\'(\t\2\2\2(-\5\6\4\5)*\f\3\2\2*")
        buf.write("+\t\3\2\2+-\5\6\4\4,&\3\2\2\2,)\3\2\2\2-\60\3\2\2\2.,")
        buf.write("\3\2\2\2./\3\2\2\2/\7\3\2\2\2\60.\3\2\2\2\61\62\7\f\2")
        buf.write("\2\62\63\5\6\4\2\63\t\3\2\2\2\7\17\25$,.")
        return buf.getvalue()


class YalangParser ( Parser ):

    grammarFileName = "Yalang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'-'", "'('", "')'", "'*'", 
                     "'/'", "'%'", "'+'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ID", 
                      "NUMBER", "STRING" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_printStmt = 3

    ruleNames =  [ "program", "statement", "expression", "printStmt" ]

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
    WS=11
    ID=12
    NUMBER=13
    STRING=14

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 9
                self.match(YalangParser.T__0)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__2) | (1 << YalangParser.T__3) | (1 << YalangParser.T__9) | (1 << YalangParser.ID) | (1 << YalangParser.NUMBER) | (1 << YalangParser.STRING))) != 0)):
                    break

            self.state = 15
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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [YalangParser.T__2, YalangParser.T__3, YalangParser.ID, YalangParser.NUMBER, YalangParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.expression(0)
                pass
            elif token in [YalangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.printStmt()
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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = YalangParser.NumberLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 22
                self.match(YalangParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = YalangParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(YalangParser.STRING)
                pass

            elif la_ == 3:
                localctx = YalangParser.IdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(YalangParser.ID)
                pass

            elif la_ == 4:
                localctx = YalangParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(YalangParser.ID)
                self.state = 26
                self.match(YalangParser.T__1)
                self.state = 27
                self.expression(5)
                pass

            elif la_ == 5:
                localctx = YalangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(YalangParser.T__2)
                self.state = 29
                self.expression(4)
                pass

            elif la_ == 6:
                localctx = YalangParser.NestedContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(YalangParser.T__3)
                self.state = 31
                self.expression(0)
                self.state = 32
                self.match(YalangParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = YalangParser.MathHighContext(self, YalangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << YalangParser.T__5) | (1 << YalangParser.T__6) | (1 << YalangParser.T__7))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        localctx.right = self.expression(3)
                        pass

                    elif la_ == 2:
                        localctx = YalangParser.MathLowContext(self, YalangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 40
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==YalangParser.T__2 or _la==YalangParser.T__8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        localctx.right = self.expression(2)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 47
            self.match(YalangParser.T__9)
            self.state = 48
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
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




