# Generated from antlr_generated/microC.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .microCParser import microCParser
else:
    from microCParser import microCParser

# This class defines a complete generic visitor for a parse tree produced by microCParser.

class microCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by microCParser#program.
    def visitProgram(self, ctx:microCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#statement.
    def visitStatement(self, ctx:microCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#ifstatement.
    def visitIfstatement(self, ctx:microCParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#whilestatement.
    def visitWhilestatement(self, ctx:microCParser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#blockstatement.
    def visitBlockstatement(self, ctx:microCParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#exprstatement.
    def visitExprstatement(self, ctx:microCParser.ExprstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#paren_expr.
    def visitParen_expr(self, ctx:microCParser.Paren_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#expr.
    def visitExpr(self, ctx:microCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#test.
    def visitTest(self, ctx:microCParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#soma.
    def visitSoma(self, ctx:microCParser.SomaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#term.
    def visitTerm(self, ctx:microCParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#idn.
    def visitIdn(self, ctx:microCParser.IdnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by microCParser#integer.
    def visitInteger(self, ctx:microCParser.IntegerContext):
        return self.visitChildren(ctx)



del microCParser