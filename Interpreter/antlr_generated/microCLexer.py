# Generated from antlr_generated/microC.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\6\16C\n\16\r\16\16\16D\3\17\6\17H\n\17\r\17\16\17I\3")
        buf.write("\20\3\20\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5")
        buf.write("\3\2c|\3\2\62;\5\2\13\f\17\17\"\"\2P\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\3!\3\2\2\2\5$\3\2\2\2\7)\3\2\2\2\t/\3\2\2")
        buf.write("\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65\3\2\2\2\21\67\3\2")
        buf.write("\2\2\239\3\2\2\2\25;\3\2\2\2\27=\3\2\2\2\31?\3\2\2\2\33")
        buf.write("B\3\2\2\2\35G\3\2\2\2\37K\3\2\2\2!\"\7k\2\2\"#\7h\2\2")
        buf.write("#\4\3\2\2\2$%\7g\2\2%&\7n\2\2&\'\7u\2\2\'(\7g\2\2(\6\3")
        buf.write("\2\2\2)*\7y\2\2*+\7j\2\2+,\7k\2\2,-\7n\2\2-.\7g\2\2.\b")
        buf.write("\3\2\2\2/\60\7}\2\2\60\n\3\2\2\2\61\62\7\177\2\2\62\f")
        buf.write("\3\2\2\2\63\64\7=\2\2\64\16\3\2\2\2\65\66\7*\2\2\66\20")
        buf.write("\3\2\2\2\678\7+\2\28\22\3\2\2\29:\7?\2\2:\24\3\2\2\2;")
        buf.write("<\7>\2\2<\26\3\2\2\2=>\7-\2\2>\30\3\2\2\2?@\7/\2\2@\32")
        buf.write("\3\2\2\2AC\t\2\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2")
        buf.write("\2\2E\34\3\2\2\2FH\t\3\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2")
        buf.write("\2IJ\3\2\2\2J\36\3\2\2\2KL\t\4\2\2LM\3\2\2\2MN\b\20\2")
        buf.write("\2N \3\2\2\2\5\2DI\3\b\2\2")
        return buf.getvalue()


class microCLexer(Lexer):

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
    T__10 = 11
    T__11 = 12
    STRING = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'{'", "'}'", "';'", "'('", "')'", 
            "'='", "'<'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "STRING", "INT", 
                  "WS" ]

    grammarFileName = "microC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


