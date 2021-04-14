from antlr4 import *
from antlr_generated.microCLexer import microCLexer
from antlr_generated.microCListener import microCListener
from antlr_generated.microCParser import microCParser
import sys


class PrintListener(microCListener):
    def enterStatement(self, ctx: microCParser.StatementContext):
        print('Code successfully interpreted!!')


def main():
    lexer = microCLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = microCParser(stream)
    tree = parser.program()
    printer = PrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
