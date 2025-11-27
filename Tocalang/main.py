import sys
from antlr4 import *
from MinhaLinguagemLexer import MinhaLinguagemLexer
from MinhaLinguagemParser import MinhaLinguagemParser
from Visitor import Visitor

def main():
    # --- CÓDIGO: CALCULAR MÉDIA ---
    # Lógica: Lê 3 notas, calcula a média (soma / 3).
    # Se média >= 7.0 -> Aprovado, senão Reprovado.
    
    codigo = """
    DECLARACOES
        n1 : REAL
        n2 : REAL
        n3 : REAL
        soma : REAL
        media : REAL
    ALGORITMO
    INICIO
        IMPRIMIR '--- SISTEMA DE NOTAS ---'
        
        IMPRIMIR 'Digite a primeira nota:'
        LER n1
        
        IMPRIMIR 'Digite a segunda nota:'
        LER n2
        
        IMPRIMIR 'Digite a terceira nota:'
        LER n3
        
        ATRIBUIR n1 + n2 + n3 A soma
        ATRIBUIR soma / 3 A media
        
        IMPRIMIR 'A sua media final foi:'
        IMPRIMIR media
        
        SE media >= 7.0 ENTAO
            IMPRIMIR 'Parabens! Voce foi APROVADO.'
        SENAO
            IMPRIMIR 'Que pena... Voce foi REPROVADO.'
        FIM
    FIM
    """

    # Execução Padrão
    lexer = MinhaLinguagemLexer(InputStream(codigo))
    stream = CommonTokenStream(lexer)
    parser = MinhaLinguagemParser(stream)
    tree = parser.programa()

    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = Visitor()
        visitor.visit(tree)
    else:
        print("ERRO: O código contém erros de sintaxe.")

if __name__ == '__main__':
    main()