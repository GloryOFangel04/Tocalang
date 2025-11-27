# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MinhaLinguagemParser import MinhaLinguagemParser
else:
    from MinhaLinguagemParser import MinhaLinguagemParser

# This class defines a complete listener for a parse tree produced by MinhaLinguagemParser.
class MinhaLinguagemListener(ParseTreeListener):

    # Enter a parse tree produced by MinhaLinguagemParser#programa.
    def enterPrograma(self, ctx:MinhaLinguagemParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#programa.
    def exitPrograma(self, ctx:MinhaLinguagemParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#declaracao.
    def enterDeclaracao(self, ctx:MinhaLinguagemParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#declaracao.
    def exitDeclaracao(self, ctx:MinhaLinguagemParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#tipo.
    def enterTipo(self, ctx:MinhaLinguagemParser.TipoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#tipo.
    def exitTipo(self, ctx:MinhaLinguagemParser.TipoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdAtribuir.
    def enterCmdAtribuir(self, ctx:MinhaLinguagemParser.CmdAtribuirContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdAtribuir.
    def exitCmdAtribuir(self, ctx:MinhaLinguagemParser.CmdAtribuirContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdLer.
    def enterCmdLer(self, ctx:MinhaLinguagemParser.CmdLerContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdLer.
    def exitCmdLer(self, ctx:MinhaLinguagemParser.CmdLerContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdImprimir.
    def enterCmdImprimir(self, ctx:MinhaLinguagemParser.CmdImprimirContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdImprimir.
    def exitCmdImprimir(self, ctx:MinhaLinguagemParser.CmdImprimirContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdSe.
    def enterCmdSe(self, ctx:MinhaLinguagemParser.CmdSeContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdSe.
    def exitCmdSe(self, ctx:MinhaLinguagemParser.CmdSeContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdEnquanto.
    def enterCmdEnquanto(self, ctx:MinhaLinguagemParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdEnquanto.
    def exitCmdEnquanto(self, ctx:MinhaLinguagemParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdPara.
    def enterCmdPara(self, ctx:MinhaLinguagemParser.CmdParaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdPara.
    def exitCmdPara(self, ctx:MinhaLinguagemParser.CmdParaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#CmdEscolha.
    def enterCmdEscolha(self, ctx:MinhaLinguagemParser.CmdEscolhaContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#CmdEscolha.
    def exitCmdEscolha(self, ctx:MinhaLinguagemParser.CmdEscolhaContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprVar.
    def enterExprVar(self, ctx:MinhaLinguagemParser.ExprVarContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprVar.
    def exitExprVar(self, ctx:MinhaLinguagemParser.ExprVarContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprAddSub.
    def enterExprAddSub(self, ctx:MinhaLinguagemParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprAddSub.
    def exitExprAddSub(self, ctx:MinhaLinguagemParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprParentesis.
    def enterExprParentesis(self, ctx:MinhaLinguagemParser.ExprParentesisContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprParentesis.
    def exitExprParentesis(self, ctx:MinhaLinguagemParser.ExprParentesisContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprRelacional.
    def enterExprRelacional(self, ctx:MinhaLinguagemParser.ExprRelacionalContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprRelacional.
    def exitExprRelacional(self, ctx:MinhaLinguagemParser.ExprRelacionalContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprMulDiv.
    def enterExprMulDiv(self, ctx:MinhaLinguagemParser.ExprMulDivContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprMulDiv.
    def exitExprMulDiv(self, ctx:MinhaLinguagemParser.ExprMulDivContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprE.
    def enterExprE(self, ctx:MinhaLinguagemParser.ExprEContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprE.
    def exitExprE(self, ctx:MinhaLinguagemParser.ExprEContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprString.
    def enterExprString(self, ctx:MinhaLinguagemParser.ExprStringContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprString.
    def exitExprString(self, ctx:MinhaLinguagemParser.ExprStringContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprOu.
    def enterExprOu(self, ctx:MinhaLinguagemParser.ExprOuContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprOu.
    def exitExprOu(self, ctx:MinhaLinguagemParser.ExprOuContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprInt.
    def enterExprInt(self, ctx:MinhaLinguagemParser.ExprIntContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprInt.
    def exitExprInt(self, ctx:MinhaLinguagemParser.ExprIntContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprReal.
    def enterExprReal(self, ctx:MinhaLinguagemParser.ExprRealContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprReal.
    def exitExprReal(self, ctx:MinhaLinguagemParser.ExprRealContext):
        pass


    # Enter a parse tree produced by MinhaLinguagemParser#ExprBool.
    def enterExprBool(self, ctx:MinhaLinguagemParser.ExprBoolContext):
        pass

    # Exit a parse tree produced by MinhaLinguagemParser#ExprBool.
    def exitExprBool(self, ctx:MinhaLinguagemParser.ExprBoolContext):
        pass



del MinhaLinguagemParser