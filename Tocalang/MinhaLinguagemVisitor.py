# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinhaLinguagemParser import MinhaLinguagemParser
else:
    from MinhaLinguagemParser import MinhaLinguagemParser

# This class defines a complete generic visitor for a parse tree produced by MinhaLinguagemParser.

class MinhaLinguagemVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MinhaLinguagemParser#programa.
    def visitPrograma(self, ctx:MinhaLinguagemParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#declaracao.
    def visitDeclaracao(self, ctx:MinhaLinguagemParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#tipo.
    def visitTipo(self, ctx:MinhaLinguagemParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdAtribuir.
    def visitCmdAtribuir(self, ctx:MinhaLinguagemParser.CmdAtribuirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdLer.
    def visitCmdLer(self, ctx:MinhaLinguagemParser.CmdLerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdImprimir.
    def visitCmdImprimir(self, ctx:MinhaLinguagemParser.CmdImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdSe.
    def visitCmdSe(self, ctx:MinhaLinguagemParser.CmdSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdEnquanto.
    def visitCmdEnquanto(self, ctx:MinhaLinguagemParser.CmdEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdPara.
    def visitCmdPara(self, ctx:MinhaLinguagemParser.CmdParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#CmdEscolha.
    def visitCmdEscolha(self, ctx:MinhaLinguagemParser.CmdEscolhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprVar.
    def visitExprVar(self, ctx:MinhaLinguagemParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprAddSub.
    def visitExprAddSub(self, ctx:MinhaLinguagemParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprParentesis.
    def visitExprParentesis(self, ctx:MinhaLinguagemParser.ExprParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprRelacional.
    def visitExprRelacional(self, ctx:MinhaLinguagemParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:MinhaLinguagemParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprE.
    def visitExprE(self, ctx:MinhaLinguagemParser.ExprEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprString.
    def visitExprString(self, ctx:MinhaLinguagemParser.ExprStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprOu.
    def visitExprOu(self, ctx:MinhaLinguagemParser.ExprOuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprInt.
    def visitExprInt(self, ctx:MinhaLinguagemParser.ExprIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprReal.
    def visitExprReal(self, ctx:MinhaLinguagemParser.ExprRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MinhaLinguagemParser#ExprBool.
    def visitExprBool(self, ctx:MinhaLinguagemParser.ExprBoolContext):
        return self.visitChildren(ctx)



del MinhaLinguagemParser