# Generated from Expr.g by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parentheses.
    def visitParentheses(self, ctx:ExprParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#binary.
    def visitBinary(self, ctx:ExprParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unary.
    def visitUnary(self, ctx:ExprParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stmt.
    def visitStmt(self, ctx:ExprParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#loop.
    def visitLoop(self, ctx:ExprParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conditional.
    def visitConditional(self, ctx:ExprParser.ConditionalContext):
        return self.visitChildren(ctx)



del ExprParser