# Generated from MinhaLinguagem.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,1,3,5,3,55,8,
        3,10,3,12,3,58,9,3,3,3,60,8,3,1,3,1,3,1,3,1,3,1,3,5,3,67,8,3,10,
        3,12,3,70,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,82,8,3,
        10,3,12,3,85,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,95,8,3,10,3,
        12,3,98,9,3,4,3,100,8,3,11,3,12,3,101,1,3,1,3,1,3,5,3,107,8,3,10,
        3,12,3,110,9,3,3,3,112,8,3,1,3,1,3,3,3,116,8,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,128,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,145,8,4,10,4,12,4,148,9,4,1,4,
        0,1,8,5,0,2,4,6,8,0,3,1,0,7,10,1,0,1,2,1,0,3,4,171,0,10,1,0,0,0,
        2,28,1,0,0,0,4,32,1,0,0,0,6,115,1,0,0,0,8,127,1,0,0,0,10,14,5,5,
        0,0,11,13,3,2,1,0,12,11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,
        1,0,0,0,15,17,1,0,0,0,16,14,1,0,0,0,17,18,5,6,0,0,18,22,5,19,0,0,
        19,21,3,6,3,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,
        0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,26,5,20,0,0,26,27,5,0,0,1,27,
        1,1,0,0,0,28,29,5,33,0,0,29,30,5,38,0,0,30,31,3,4,2,0,31,3,1,0,0,
        0,32,33,7,0,0,0,33,5,1,0,0,0,34,35,5,11,0,0,35,36,3,8,4,0,36,37,
        5,12,0,0,37,38,5,33,0,0,38,116,1,0,0,0,39,40,5,13,0,0,40,116,5,33,
        0,0,41,42,5,14,0,0,42,116,3,8,4,0,43,44,5,15,0,0,44,45,3,8,4,0,45,
        49,5,16,0,0,46,48,3,6,3,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,
        0,0,49,50,1,0,0,0,50,59,1,0,0,0,51,49,1,0,0,0,52,56,5,17,0,0,53,
        55,3,6,3,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,
        0,57,60,1,0,0,0,58,56,1,0,0,0,59,52,1,0,0,0,59,60,1,0,0,0,60,61,
        1,0,0,0,61,62,5,20,0,0,62,116,1,0,0,0,63,64,5,18,0,0,64,68,3,8,4,
        0,65,67,3,6,3,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,
        1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,20,0,0,72,116,1,0,0,
        0,73,74,5,23,0,0,74,75,5,33,0,0,75,76,5,24,0,0,76,77,3,8,4,0,77,
        78,5,25,0,0,78,79,3,8,4,0,79,83,5,26,0,0,80,82,3,6,3,0,81,80,1,0,
        0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,
        1,0,0,0,86,87,5,20,0,0,87,116,1,0,0,0,88,89,5,27,0,0,89,99,3,8,4,
        0,90,91,5,28,0,0,91,92,3,8,4,0,92,96,5,38,0,0,93,95,3,6,3,0,94,93,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,100,1,0,0,0,
        98,96,1,0,0,0,99,90,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,
        1,0,0,0,102,111,1,0,0,0,103,104,5,29,0,0,104,108,5,38,0,0,105,107,
        3,6,3,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,
        1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,103,1,0,0,0,111,112,
        1,0,0,0,112,113,1,0,0,0,113,114,5,20,0,0,114,116,1,0,0,0,115,34,
        1,0,0,0,115,39,1,0,0,0,115,41,1,0,0,0,115,43,1,0,0,0,115,63,1,0,
        0,0,115,73,1,0,0,0,115,88,1,0,0,0,116,7,1,0,0,0,117,118,6,4,-1,0,
        118,128,5,31,0,0,119,128,5,32,0,0,120,128,5,30,0,0,121,128,5,33,
        0,0,122,128,5,34,0,0,123,124,5,39,0,0,124,125,3,8,4,0,125,126,5,
        40,0,0,126,128,1,0,0,0,127,117,1,0,0,0,127,119,1,0,0,0,127,120,1,
        0,0,0,127,121,1,0,0,0,127,122,1,0,0,0,127,123,1,0,0,0,128,146,1,
        0,0,0,129,130,10,11,0,0,130,131,7,1,0,0,131,145,3,8,4,12,132,133,
        10,10,0,0,133,134,7,2,0,0,134,145,3,8,4,11,135,136,10,9,0,0,136,
        137,5,37,0,0,137,145,3,8,4,10,138,139,10,8,0,0,139,140,5,21,0,0,
        140,145,3,8,4,9,141,142,10,7,0,0,142,143,5,22,0,0,143,145,3,8,4,
        8,144,129,1,0,0,0,144,132,1,0,0,0,144,135,1,0,0,0,144,138,1,0,0,
        0,144,141,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,
        0,147,9,1,0,0,0,148,146,1,0,0,0,15,14,22,49,56,59,68,83,96,101,108,
        111,115,127,144,146
    ]

class MinhaLinguagemParser ( Parser ):

    grammarFileName = "MinhaLinguagem.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'DECLARACOES'", 
                     "'ALGORITMO'", "'INTEIRO'", "'REAL'", "'BOOLEANO'", 
                     "'TEXTO'", "'ATRIBUIR'", "'A'", "'LER'", "'IMPRIMIR'", 
                     "'SE'", "'ENTAO'", "'SENAO'", "'ENQUANTO'", "'INICIO'", 
                     "'FIM'", "'E'", "'OU'", "'PARA'", "'DE'", "'ATE'", 
                     "'FACA'", "'ESCOLHA'", "'CASO'", "'PADRAO'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "K_DECLARACOES", "K_ALGORITMO", "K_INTEIRO", 
                      "K_REAL", "K_BOOLEANO", "K_TEXTO", "K_ATRIBUIR", "K_A", 
                      "K_LER", "K_IMPRIMIR", "K_SE", "K_ENTAO", "K_SENAO", 
                      "K_ENQUANTO", "K_INICIO", "K_FIM", "K_E", "K_OU", 
                      "K_PARA", "K_DE", "K_ATE", "K_FACA", "K_ESCOLHA", 
                      "K_CASO", "K_PADRAO", "BOOL_LIT", "NUMINT", "NUMREAL", 
                      "VARIAVEL", "CADEIA", "COMENTARIO", "WS", "OP_REL", 
                      "DELIM", "ABREPAR", "FECHAPAR" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_tipo = 2
    RULE_comando = 3
    RULE_expr = 4

    ruleNames =  [ "programa", "declaracao", "tipo", "comando", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    K_DECLARACOES=5
    K_ALGORITMO=6
    K_INTEIRO=7
    K_REAL=8
    K_BOOLEANO=9
    K_TEXTO=10
    K_ATRIBUIR=11
    K_A=12
    K_LER=13
    K_IMPRIMIR=14
    K_SE=15
    K_ENTAO=16
    K_SENAO=17
    K_ENQUANTO=18
    K_INICIO=19
    K_FIM=20
    K_E=21
    K_OU=22
    K_PARA=23
    K_DE=24
    K_ATE=25
    K_FACA=26
    K_ESCOLHA=27
    K_CASO=28
    K_PADRAO=29
    BOOL_LIT=30
    NUMINT=31
    NUMREAL=32
    VARIAVEL=33
    CADEIA=34
    COMENTARIO=35
    WS=36
    OP_REL=37
    DELIM=38
    ABREPAR=39
    FECHAPAR=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DECLARACOES(self):
            return self.getToken(MinhaLinguagemParser.K_DECLARACOES, 0)

        def K_ALGORITMO(self):
            return self.getToken(MinhaLinguagemParser.K_ALGORITMO, 0)

        def K_INICIO(self):
            return self.getToken(MinhaLinguagemParser.K_INICIO, 0)

        def K_FIM(self):
            return self.getToken(MinhaLinguagemParser.K_FIM, 0)

        def EOF(self):
            return self.getToken(MinhaLinguagemParser.EOF, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.DeclaracaoContext,i)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MinhaLinguagemParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(MinhaLinguagemParser.K_DECLARACOES)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 11
                self.declaracao()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(MinhaLinguagemParser.K_ALGORITMO)
            self.state = 18
            self.match(MinhaLinguagemParser.K_INICIO)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                self.state = 19
                self.comando()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(MinhaLinguagemParser.K_FIM)
            self.state = 26
            self.match(MinhaLinguagemParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIAVEL(self):
            return self.getToken(MinhaLinguagemParser.VARIAVEL, 0)

        def DELIM(self):
            return self.getToken(MinhaLinguagemParser.DELIM, 0)

        def tipo(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.TipoContext,0)


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = MinhaLinguagemParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MinhaLinguagemParser.VARIAVEL)
            self.state = 29
            self.match(MinhaLinguagemParser.DELIM)
            self.state = 30
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_INTEIRO(self):
            return self.getToken(MinhaLinguagemParser.K_INTEIRO, 0)

        def K_REAL(self):
            return self.getToken(MinhaLinguagemParser.K_REAL, 0)

        def K_BOOLEANO(self):
            return self.getToken(MinhaLinguagemParser.K_BOOLEANO, 0)

        def K_TEXTO(self):
            return self.getToken(MinhaLinguagemParser.K_TEXTO, 0)

        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = MinhaLinguagemParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_comando

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CmdParaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_PARA(self):
            return self.getToken(MinhaLinguagemParser.K_PARA, 0)
        def VARIAVEL(self):
            return self.getToken(MinhaLinguagemParser.VARIAVEL, 0)
        def K_DE(self):
            return self.getToken(MinhaLinguagemParser.K_DE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)

        def K_ATE(self):
            return self.getToken(MinhaLinguagemParser.K_ATE, 0)
        def K_FACA(self):
            return self.getToken(MinhaLinguagemParser.K_FACA, 0)
        def K_FIM(self):
            return self.getToken(MinhaLinguagemParser.K_FIM, 0)
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdPara" ):
                listener.enterCmdPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdPara" ):
                listener.exitCmdPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdPara" ):
                return visitor.visitCmdPara(self)
            else:
                return visitor.visitChildren(self)


    class CmdEscolhaContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_ESCOLHA(self):
            return self.getToken(MinhaLinguagemParser.K_ESCOLHA, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)

        def K_FIM(self):
            return self.getToken(MinhaLinguagemParser.K_FIM, 0)
        def K_CASO(self, i:int=None):
            if i is None:
                return self.getTokens(MinhaLinguagemParser.K_CASO)
            else:
                return self.getToken(MinhaLinguagemParser.K_CASO, i)
        def DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(MinhaLinguagemParser.DELIM)
            else:
                return self.getToken(MinhaLinguagemParser.DELIM, i)
        def K_PADRAO(self):
            return self.getToken(MinhaLinguagemParser.K_PADRAO, 0)
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEscolha" ):
                listener.enterCmdEscolha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEscolha" ):
                listener.exitCmdEscolha(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdEscolha" ):
                return visitor.visitCmdEscolha(self)
            else:
                return visitor.visitChildren(self)


    class CmdImprimirContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_IMPRIMIR(self):
            return self.getToken(MinhaLinguagemParser.K_IMPRIMIR, 0)
        def expr(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdImprimir" ):
                listener.enterCmdImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdImprimir" ):
                listener.exitCmdImprimir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdImprimir" ):
                return visitor.visitCmdImprimir(self)
            else:
                return visitor.visitChildren(self)


    class CmdEnquantoContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_ENQUANTO(self):
            return self.getToken(MinhaLinguagemParser.K_ENQUANTO, 0)
        def expr(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,0)

        def K_FIM(self):
            return self.getToken(MinhaLinguagemParser.K_FIM, 0)
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEnquanto" ):
                listener.enterCmdEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEnquanto" ):
                listener.exitCmdEnquanto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdEnquanto" ):
                return visitor.visitCmdEnquanto(self)
            else:
                return visitor.visitChildren(self)


    class CmdAtribuirContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_ATRIBUIR(self):
            return self.getToken(MinhaLinguagemParser.K_ATRIBUIR, 0)
        def expr(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,0)

        def K_A(self):
            return self.getToken(MinhaLinguagemParser.K_A, 0)
        def VARIAVEL(self):
            return self.getToken(MinhaLinguagemParser.VARIAVEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAtribuir" ):
                listener.enterCmdAtribuir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAtribuir" ):
                listener.exitCmdAtribuir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdAtribuir" ):
                return visitor.visitCmdAtribuir(self)
            else:
                return visitor.visitChildren(self)


    class CmdLerContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_LER(self):
            return self.getToken(MinhaLinguagemParser.K_LER, 0)
        def VARIAVEL(self):
            return self.getToken(MinhaLinguagemParser.VARIAVEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdLer" ):
                listener.enterCmdLer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdLer" ):
                listener.exitCmdLer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdLer" ):
                return visitor.visitCmdLer(self)
            else:
                return visitor.visitChildren(self)


    class CmdSeContext(ComandoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ComandoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def K_SE(self):
            return self.getToken(MinhaLinguagemParser.K_SE, 0)
        def expr(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,0)

        def K_ENTAO(self):
            return self.getToken(MinhaLinguagemParser.K_ENTAO, 0)
        def K_FIM(self):
            return self.getToken(MinhaLinguagemParser.K_FIM, 0)
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ComandoContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ComandoContext,i)

        def K_SENAO(self):
            return self.getToken(MinhaLinguagemParser.K_SENAO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdSe" ):
                listener.enterCmdSe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdSe" ):
                listener.exitCmdSe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdSe" ):
                return visitor.visitCmdSe(self)
            else:
                return visitor.visitChildren(self)



    def comando(self):

        localctx = MinhaLinguagemParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comando)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = MinhaLinguagemParser.CmdAtribuirContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(MinhaLinguagemParser.K_ATRIBUIR)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(MinhaLinguagemParser.K_A)
                self.state = 37
                self.match(MinhaLinguagemParser.VARIAVEL)
                pass
            elif token in [13]:
                localctx = MinhaLinguagemParser.CmdLerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(MinhaLinguagemParser.K_LER)
                self.state = 40
                self.match(MinhaLinguagemParser.VARIAVEL)
                pass
            elif token in [14]:
                localctx = MinhaLinguagemParser.CmdImprimirContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(MinhaLinguagemParser.K_IMPRIMIR)
                self.state = 42
                self.expr(0)
                pass
            elif token in [15]:
                localctx = MinhaLinguagemParser.CmdSeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(MinhaLinguagemParser.K_SE)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(MinhaLinguagemParser.K_ENTAO)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                    self.state = 46
                    self.comando()
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 52
                    self.match(MinhaLinguagemParser.K_SENAO)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                        self.state = 53
                        self.comando()
                        self.state = 58
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 61
                self.match(MinhaLinguagemParser.K_FIM)
                pass
            elif token in [18]:
                localctx = MinhaLinguagemParser.CmdEnquantoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(MinhaLinguagemParser.K_ENQUANTO)
                self.state = 64
                self.expr(0)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                    self.state = 65
                    self.comando()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self.match(MinhaLinguagemParser.K_FIM)
                pass
            elif token in [23]:
                localctx = MinhaLinguagemParser.CmdParaContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(MinhaLinguagemParser.K_PARA)
                self.state = 74
                self.match(MinhaLinguagemParser.VARIAVEL)
                self.state = 75
                self.match(MinhaLinguagemParser.K_DE)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(MinhaLinguagemParser.K_ATE)
                self.state = 78
                self.expr(0)
                self.state = 79
                self.match(MinhaLinguagemParser.K_FACA)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                    self.state = 80
                    self.comando()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.match(MinhaLinguagemParser.K_FIM)
                pass
            elif token in [27]:
                localctx = MinhaLinguagemParser.CmdEscolhaContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.match(MinhaLinguagemParser.K_ESCOLHA)
                self.state = 89
                self.expr(0)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 90
                    self.match(MinhaLinguagemParser.K_CASO)
                    self.state = 91
                    self.expr(0)
                    self.state = 92
                    self.match(MinhaLinguagemParser.DELIM)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                        self.state = 93
                        self.comando()
                        self.state = 98
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==28):
                        break

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 103
                    self.match(MinhaLinguagemParser.K_PADRAO)
                    self.state = 104
                    self.match(MinhaLinguagemParser.DELIM)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 142927872) != 0):
                        self.state = 105
                        self.comando()
                        self.state = 110
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 113
                self.match(MinhaLinguagemParser.K_FIM)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MinhaLinguagemParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprVarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIAVEL(self):
            return self.getToken(MinhaLinguagemParser.VARIAVEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVar" ):
                listener.enterExprVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVar" ):
                listener.exitExprVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVar" ):
                return visitor.visitExprVar(self)
            else:
                return visitor.visitChildren(self)


    class ExprAddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAddSub" ):
                listener.enterExprAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAddSub" ):
                listener.exitExprAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABREPAR(self):
            return self.getToken(MinhaLinguagemParser.ABREPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,0)

        def FECHAPAR(self):
            return self.getToken(MinhaLinguagemParser.FECHAPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParentesis" ):
                listener.enterExprParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParentesis" ):
                listener.exitExprParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParentesis" ):
                return visitor.visitExprParentesis(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelacionalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)

        def OP_REL(self):
            return self.getToken(MinhaLinguagemParser.OP_REL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacional" ):
                listener.enterExprRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacional" ):
                listener.exitExprRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacional" ):
                return visitor.visitExprRelacional(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMulDiv" ):
                listener.enterExprMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMulDiv" ):
                listener.exitExprMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprEContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)

        def K_E(self):
            return self.getToken(MinhaLinguagemParser.K_E, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprE" ):
                listener.enterExprE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprE" ):
                listener.exitExprE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprE" ):
                return visitor.visitExprE(self)
            else:
                return visitor.visitChildren(self)


    class ExprStringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CADEIA(self):
            return self.getToken(MinhaLinguagemParser.CADEIA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprString" ):
                listener.enterExprString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprString" ):
                listener.exitExprString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprString" ):
                return visitor.visitExprString(self)
            else:
                return visitor.visitChildren(self)


    class ExprOuContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MinhaLinguagemParser.ExprContext)
            else:
                return self.getTypedRuleContext(MinhaLinguagemParser.ExprContext,i)

        def K_OU(self):
            return self.getToken(MinhaLinguagemParser.K_OU, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOu" ):
                listener.enterExprOu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOu" ):
                listener.exitExprOu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOu" ):
                return visitor.visitExprOu(self)
            else:
                return visitor.visitChildren(self)


    class ExprIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMINT(self):
            return self.getToken(MinhaLinguagemParser.NUMINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInt" ):
                listener.enterExprInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInt" ):
                listener.exitExprInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInt" ):
                return visitor.visitExprInt(self)
            else:
                return visitor.visitChildren(self)


    class ExprRealContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMREAL(self):
            return self.getToken(MinhaLinguagemParser.NUMREAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprReal" ):
                listener.enterExprReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprReal" ):
                listener.exitExprReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReal" ):
                return visitor.visitExprReal(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MinhaLinguagemParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LIT(self):
            return self.getToken(MinhaLinguagemParser.BOOL_LIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBool" ):
                listener.enterExprBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBool" ):
                listener.exitExprBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBool" ):
                return visitor.visitExprBool(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MinhaLinguagemParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = MinhaLinguagemParser.ExprIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 118
                self.match(MinhaLinguagemParser.NUMINT)
                pass
            elif token in [32]:
                localctx = MinhaLinguagemParser.ExprRealContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(MinhaLinguagemParser.NUMREAL)
                pass
            elif token in [30]:
                localctx = MinhaLinguagemParser.ExprBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(MinhaLinguagemParser.BOOL_LIT)
                pass
            elif token in [33]:
                localctx = MinhaLinguagemParser.ExprVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(MinhaLinguagemParser.VARIAVEL)
                pass
            elif token in [34]:
                localctx = MinhaLinguagemParser.ExprStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(MinhaLinguagemParser.CADEIA)
                pass
            elif token in [39]:
                localctx = MinhaLinguagemParser.ExprParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(MinhaLinguagemParser.ABREPAR)
                self.state = 124
                self.expr(0)
                self.state = 125
                self.match(MinhaLinguagemParser.FECHAPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 144
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MinhaLinguagemParser.ExprMulDivContext(self, MinhaLinguagemParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = MinhaLinguagemParser.ExprAddSubContext(self, MinhaLinguagemParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 133
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = MinhaLinguagemParser.ExprRelacionalContext(self, MinhaLinguagemParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 136
                        localctx.op = self.match(MinhaLinguagemParser.OP_REL)
                        self.state = 137
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = MinhaLinguagemParser.ExprEContext(self, MinhaLinguagemParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 139
                        self.match(MinhaLinguagemParser.K_E)
                        self.state = 140
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = MinhaLinguagemParser.ExprOuContext(self, MinhaLinguagemParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 142
                        self.match(MinhaLinguagemParser.K_OU)
                        self.state = 143
                        self.expr(8)
                        pass

             
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




