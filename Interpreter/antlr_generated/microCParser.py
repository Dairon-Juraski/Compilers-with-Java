# Generated from antlr_generated/microC.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\3\3\5\3&\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\7\6\65\n\6\f\6\16\68\13\6\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tH\n\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\nO\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\7\13Z\n\13\f\13\16\13]\13\13\3\f\3\f\3\f\5\fb\n")
        buf.write("\f\3\r\3\r\3\16\3\16\3\16\2\3\24\17\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\2\2\2f\2\35\3\2\2\2\4%\3\2\2\2\6\'\3\2")
        buf.write("\2\2\b.\3\2\2\2\n\62\3\2\2\2\f;\3\2\2\2\16>\3\2\2\2\20")
        buf.write("G\3\2\2\2\22N\3\2\2\2\24P\3\2\2\2\26a\3\2\2\2\30c\3\2")
        buf.write("\2\2\32e\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!&\5\6\4\2\"")
        buf.write("&\5\b\5\2#&\5\n\6\2$&\5\f\7\2%!\3\2\2\2%\"\3\2\2\2%#\3")
        buf.write("\2\2\2%$\3\2\2\2&\5\3\2\2\2\'(\7\3\2\2()\5\16\b\2),\5")
        buf.write("\4\3\2*+\7\4\2\2+-\5\4\3\2,*\3\2\2\2,-\3\2\2\2-\7\3\2")
        buf.write("\2\2./\7\5\2\2/\60\5\16\b\2\60\61\5\4\3\2\61\t\3\2\2\2")
        buf.write("\62\66\7\6\2\2\63\65\5\4\3\2\64\63\3\2\2\2\658\3\2\2\2")
        buf.write("\66\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29")
        buf.write(":\7\7\2\2:\13\3\2\2\2;<\5\20\t\2<=\7\b\2\2=\r\3\2\2\2")
        buf.write(">?\7\t\2\2?@\5\20\t\2@A\7\n\2\2A\17\3\2\2\2BH\5\22\n\2")
        buf.write("CD\5\30\r\2DE\7\13\2\2EF\5\20\t\2FH\3\2\2\2GB\3\2\2\2")
        buf.write("GC\3\2\2\2H\21\3\2\2\2IO\5\24\13\2JK\5\24\13\2KL\7\f\2")
        buf.write("\2LM\5\24\13\2MO\3\2\2\2NI\3\2\2\2NJ\3\2\2\2O\23\3\2\2")
        buf.write("\2PQ\b\13\1\2QR\5\26\f\2R[\3\2\2\2ST\f\4\2\2TU\7\r\2\2")
        buf.write("UZ\5\26\f\2VW\f\3\2\2WX\7\16\2\2XZ\5\26\f\2YS\3\2\2\2")
        buf.write("YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\25\3\2\2\2")
        buf.write("][\3\2\2\2^b\5\30\r\2_b\5\32\16\2`b\5\16\b\2a^\3\2\2\2")
        buf.write("a_\3\2\2\2a`\3\2\2\2b\27\3\2\2\2cd\7\17\2\2d\31\3\2\2")
        buf.write("\2ef\7\20\2\2f\33\3\2\2\2\13\37%,\66GNY[a")
        return buf.getvalue()


class microCParser ( Parser ):

    grammarFileName = "microC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'{'", "'}'", 
                     "';'", "'('", "')'", "'='", "'<'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_ifstatement = 2
    RULE_whilestatement = 3
    RULE_blockstatement = 4
    RULE_exprstatement = 5
    RULE_paren_expr = 6
    RULE_expr = 7
    RULE_test = 8
    RULE_soma = 9
    RULE_term = 10
    RULE_idn = 11
    RULE_integer = 12

    ruleNames =  [ "program", "statement", "ifstatement", "whilestatement", 
                   "blockstatement", "exprstatement", "paren_expr", "expr", 
                   "test", "soma", "term", "idn", "integer" ]

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
    STRING=13
    INT=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(microCParser.StatementContext)
            else:
                return self.getTypedRuleContext(microCParser.StatementContext,i)


        def getRuleIndex(self):
            return microCParser.RULE_program

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

        localctx = microCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << microCParser.T__0) | (1 << microCParser.T__2) | (1 << microCParser.T__3) | (1 << microCParser.T__6) | (1 << microCParser.STRING) | (1 << microCParser.INT))) != 0)):
                    break

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

        def ifstatement(self):
            return self.getTypedRuleContext(microCParser.IfstatementContext,0)


        def whilestatement(self):
            return self.getTypedRuleContext(microCParser.WhilestatementContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(microCParser.BlockstatementContext,0)


        def exprstatement(self):
            return self.getTypedRuleContext(microCParser.ExprstatementContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_statement

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

        localctx = microCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [microCParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.ifstatement()
                pass
            elif token in [microCParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.whilestatement()
                pass
            elif token in [microCParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.blockstatement()
                pass
            elif token in [microCParser.T__6, microCParser.STRING, microCParser.INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.exprstatement()
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


    class IfstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paren_expr(self):
            return self.getTypedRuleContext(microCParser.Paren_exprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(microCParser.StatementContext)
            else:
                return self.getTypedRuleContext(microCParser.StatementContext,i)


        def getRuleIndex(self):
            return microCParser.RULE_ifstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstatement" ):
                listener.enterIfstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstatement" ):
                listener.exitIfstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstatement" ):
                return visitor.visitIfstatement(self)
            else:
                return visitor.visitChildren(self)




    def ifstatement(self):

        localctx = microCParser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(microCParser.T__0)
            self.state = 38
            self.paren_expr()
            self.state = 39
            self.statement()
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 40
                self.match(microCParser.T__1)
                self.state = 41
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paren_expr(self):
            return self.getTypedRuleContext(microCParser.Paren_exprContext,0)


        def statement(self):
            return self.getTypedRuleContext(microCParser.StatementContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_whilestatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestatement" ):
                listener.enterWhilestatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestatement" ):
                listener.exitWhilestatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestatement" ):
                return visitor.visitWhilestatement(self)
            else:
                return visitor.visitChildren(self)




    def whilestatement(self):

        localctx = microCParser.WhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(microCParser.T__2)
            self.state = 45
            self.paren_expr()
            self.state = 46
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(microCParser.StatementContext)
            else:
                return self.getTypedRuleContext(microCParser.StatementContext,i)


        def getRuleIndex(self):
            return microCParser.RULE_blockstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockstatement" ):
                listener.enterBlockstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockstatement" ):
                listener.exitBlockstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstatement" ):
                return visitor.visitBlockstatement(self)
            else:
                return visitor.visitChildren(self)




    def blockstatement(self):

        localctx = microCParser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blockstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(microCParser.T__3)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << microCParser.T__0) | (1 << microCParser.T__2) | (1 << microCParser.T__3) | (1 << microCParser.T__6) | (1 << microCParser.STRING) | (1 << microCParser.INT))) != 0):
                self.state = 49
                self.statement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(microCParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(microCParser.ExprContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_exprstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprstatement" ):
                listener.enterExprstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprstatement" ):
                listener.exitExprstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprstatement" ):
                return visitor.visitExprstatement(self)
            else:
                return visitor.visitChildren(self)




    def exprstatement(self):

        localctx = microCParser.ExprstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exprstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.expr()
            self.state = 58
            self.match(microCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paren_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(microCParser.ExprContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_paren_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen_expr" ):
                listener.enterParen_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen_expr" ):
                listener.exitParen_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen_expr" ):
                return visitor.visitParen_expr(self)
            else:
                return visitor.visitChildren(self)




    def paren_expr(self):

        localctx = microCParser.Paren_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paren_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(microCParser.T__6)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(microCParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(microCParser.TestContext,0)


        def idn(self):
            return self.getTypedRuleContext(microCParser.IdnContext,0)


        def expr(self):
            return self.getTypedRuleContext(microCParser.ExprContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = microCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.idn()
                self.state = 66
                self.match(microCParser.T__8)
                self.state = 67
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def soma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(microCParser.SomaContext)
            else:
                return self.getTypedRuleContext(microCParser.SomaContext,i)


        def getRuleIndex(self):
            return microCParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest" ):
                return visitor.visitTest(self)
            else:
                return visitor.visitChildren(self)




    def test(self):

        localctx = microCParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_test)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.soma(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.soma(0)
                self.state = 73
                self.match(microCParser.T__9)
                self.state = 74
                self.soma(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SomaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(microCParser.TermContext,0)


        def soma(self):
            return self.getTypedRuleContext(microCParser.SomaContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_soma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma" ):
                listener.enterSoma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma" ):
                listener.exitSoma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoma" ):
                return visitor.visitSoma(self)
            else:
                return visitor.visitChildren(self)



    def soma(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = microCParser.SomaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_soma, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = microCParser.SomaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_soma)
                        self.state = 81
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 82
                        self.match(microCParser.T__10)
                        self.state = 83
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = microCParser.SomaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_soma)
                        self.state = 84
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 85
                        self.match(microCParser.T__11)
                        self.state = 86
                        self.term()
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idn(self):
            return self.getTypedRuleContext(microCParser.IdnContext,0)


        def integer(self):
            return self.getTypedRuleContext(microCParser.IntegerContext,0)


        def paren_expr(self):
            return self.getTypedRuleContext(microCParser.Paren_exprContext,0)


        def getRuleIndex(self):
            return microCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = microCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [microCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.idn()
                pass
            elif token in [microCParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.integer()
                pass
            elif token in [microCParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.paren_expr()
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


    class IdnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(microCParser.STRING, 0)

        def getRuleIndex(self):
            return microCParser.RULE_idn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdn" ):
                listener.enterIdn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdn" ):
                listener.exitIdn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdn" ):
                return visitor.visitIdn(self)
            else:
                return visitor.visitChildren(self)




    def idn(self):

        localctx = microCParser.IdnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(microCParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(microCParser.INT, 0)

        def getRuleIndex(self):
            return microCParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = microCParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(microCParser.INT)
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
        self._predicates[9] = self.soma_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def soma_sempred(self, localctx:SomaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




