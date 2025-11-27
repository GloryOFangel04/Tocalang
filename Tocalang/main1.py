import sys
from antlr4 import *
from MinhaLinguagemLexer import MinhaLinguagemLexer
from MinhaLinguagemParser import MinhaLinguagemParser
from Visitor import Visitor

def main():
   
    if len(sys.argv) < 2:
        print("Erro: Você deve informar o arquivo a ser compilado.")
        print("Uso correto: python main.py <nome_do_arquivo>")
        return

   
    nome_arquivo = sys.argv[1]

    try:
        
        input_stream = FileStream(nome_arquivo, encoding='utf-8')
        
        
        lexer = MinhaLinguagemLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MinhaLinguagemParser(stream)
        tree = parser.programa()

        
        if parser.getNumberOfSyntaxErrors() == 0:
            visitor = Visitor()
            visitor.visit(tree)
        else:
            print("ERRO: O código contém erros de sintaxe e não pode ser executado.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta.")

if __name__ == '__main__':
    main()