# Generated from antlr_generated/microC.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .microCParser import microCParser
else:
    from microCParser import microCParser

# This class defines a complete listener for a parse tree produced by microCParser.
class microCListener(ParseTreeListener):

    # Enter a parse tree produced by microCParser#program.
    def enterProgram(self, ctx:microCParser.ProgramContext):
        pass

    # Exit a parse tree produced by microCParser#program.
    def exitProgram(self, ctx:microCParser.ProgramContext):
        pass


    # Enter a parse tree produced by microCParser#statement.
    def enterStatement(self, ctx:microCParser.StatementContext):
        pass

    # Exit a parse tree produced by microCParser#statement.
    def exitStatement(self, ctx:microCParser.StatementContext):
        pass


    # Enter a parse tree produced by microCParser#ifstatement.
    def enterIfstatement(self, ctx:microCParser.IfstatementContext):
        pass

    # Exit a parse tree produced by microCParser#ifstatement.
    def exitIfstatement(self, ctx:microCParser.IfstatementContext):
        pass


    # Enter a parse tree produced by microCParser#whilestatement.
    def enterWhilestatement(self, ctx:microCParser.WhilestatementContext):
        pass

    # Exit a parse tree produced by microCParser#whilestatement.
    def exitWhilestatement(self, ctx:microCParser.WhilestatementContext):
        pass


    # Enter a parse tree produced by microCParser#blockstatement.
    def enterBlockstatement(self, ctx:microCParser.BlockstatementContext):
        pass

    # Exit a parse tree produced by microCParser#blockstatement.
    def exitBlockstatement(self, ctx:microCParser.BlockstatementContext):
        pass


    # Enter a parse tree produced by microCParser#exprstatement.
    def enterExprstatement(self, ctx:microCParser.ExprstatementContext):
        pass

    # Exit a parse tree produced by microCParser#exprstatement.
    def exitExprstatement(self, ctx:microCParser.ExprstatementContext):
        pass


    # Enter a parse tree produced by microCParser#paren_expr.
    def enterParen_expr(self, ctx:microCParser.Paren_exprContext):
        pass

    # Exit a parse tree produced by microCParser#paren_expr.
    def exitParen_expr(self, ctx:microCParser.Paren_exprContext):
        pass


    # Enter a parse tree produced by microCParser#expr.
    def enterExpr(self, ctx:microCParser.ExprContext):
        pass

    # Exit a parse tree produced by microCParser#expr.
    def exitExpr(self, ctx:microCParser.ExprContext):
        pass


    # Enter a parse tree produced by microCParser#test.
    def enterTest(self, ctx:microCParser.TestContext):
        pass

    # Exit a parse tree produced by microCParser#test.
    def exitTest(self, ctx:microCParser.TestContext):
        pass


    # Enter a parse tree produced by microCParser#soma.
    def enterSoma(self, ctx:microCParser.SomaContext):
        pass

    # Exit a parse tree produced by microCParser#soma.
    def exitSoma(self, ctx:microCParser.SomaContext):
        pass


    # Enter a parse tree produced by microCParser#term.
    def enterTerm(self, ctx:microCParser.TermContext):
        pass

    # Exit a parse tree produced by microCParser#term.
    def exitTerm(self, ctx:microCParser.TermContext):
        pass


    # Enter a parse tree produced by microCParser#idn.
    def enterIdn(self, ctx:microCParser.IdnContext):
        pass

    # Exit a parse tree produced by microCParser#idn.
    def exitIdn(self, ctx:microCParser.IdnContext):
        pass


    # Enter a parse tree produced by microCParser#integer.
    def enterInteger(self, ctx:microCParser.IntegerContext):
        pass

    # Exit a parse tree produced by microCParser#integer.
    def exitInteger(self, ctx:microCParser.IntegerContext):
        pass



del microCParser