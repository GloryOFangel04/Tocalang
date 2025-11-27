from MinhaLinguagemVisitor import MinhaLinguagemVisitor
from MinhaLinguagemParser import MinhaLinguagemParser

class Visitor(MinhaLinguagemVisitor):
    def __init__(self):
        self.variaveis = {}
        self.tipos = {}

    # --- DECLARAÇÃO DE VARIÁVEIS ---
    def visitDeclaracao(self, ctx):
        nome = ctx.VARIAVEL().getText()
        tipo_token = ctx.tipo().getText()
        
        if tipo_token == 'INTEIRO':
            self.variaveis[nome] = 0
            self.tipos[nome] = 'INTEIRO'
        elif tipo_token == 'REAL':
            self.variaveis[nome] = 0.0
            self.tipos[nome] = 'REAL'
        elif tipo_token == 'BOOLEANO':
            self.variaveis[nome] = False
            self.tipos[nome] = 'BOOLEANO'
        elif tipo_token == 'TEXTO':
            self.variaveis[nome] = ""
            self.tipos[nome] = 'TEXTO'
        return self.visitChildren(ctx)

    # --- COMANDOS BÁSICOS ---
    def visitCmdAtribuir(self, ctx):
        nome = ctx.VARIAVEL().getText()
        valor = self.visit(ctx.expr())
        if nome in self.variaveis:
            self.variaveis[nome] = valor
        else:
            print(f"ERRO: Variável '{nome}' não declarada.")
        return None

    def visitCmdLer(self, ctx):
        nome = ctx.VARIAVEL().getText()
        if nome in self.variaveis:
            valor_input = input() 
            try:
                tipo = self.tipos[nome]
                if tipo == 'INTEIRO':
                    self.variaveis[nome] = int(valor_input)
                elif tipo == 'REAL':
                    self.variaveis[nome] = float(valor_input)
                elif tipo == 'BOOLEANO':
                    self.variaveis[nome] = (valor_input.lower() == 'verdadeiro')
                else: 
                    self.variaveis[nome] = valor_input
            except ValueError:
                print(f"ERRO: Valor digitado inválido para o tipo {tipo}.")
        else:
            print(f"ERRO: Variável '{nome}' não existe.")
        return None

    def visitCmdImprimir(self, ctx):
        valor = self.visit(ctx.expr())
        if valor is True:
            print("VERDADEIRO")
        elif valor is False:
            print("FALSO")
        else:
            print(valor)
        return None

    # --- ESTRUTURAS DE CONTROLE ---

    def visitCmdSe(self, ctx):
        condicao = self.visit(ctx.expr())
        executando_entao = False
        executando_senao = False

        if condicao:
        
            for filho in ctx.children:
                if filho.getText() == 'ENTAO':
                    executando_entao = True
                    continue
                if filho.getText() == 'SENAO' or filho.getText() == 'FIM':
                    executando_entao = False
                
                if executando_entao and isinstance(filho, MinhaLinguagemParser.ComandoContext):
                    self.visit(filho)
        else:
          
            for filho in ctx.children:
                if filho.getText() == 'SENAO':
                    executando_senao = True
                    continue
                if filho.getText() == 'FIM':
                    executando_senao = False
                
                if executando_senao and isinstance(filho, MinhaLinguagemParser.ComandoContext):
                    self.visit(filho)
        return None

    def visitCmdEnquanto(self, ctx):
        while self.visit(ctx.expr()):
            for cmd in ctx.comando():
                self.visit(cmd)
        return None

    def visitCmdPara(self, ctx):
        nome_var = ctx.VARIAVEL().getText()
        inicio = self.visit(ctx.expr(0))
        fim = self.visit(ctx.expr(1))
        
        self.variaveis[nome_var] = inicio
        
        while self.variaveis[nome_var] <= fim:
            for cmd in ctx.comando():
                self.visit(cmd)
            self.variaveis[nome_var] += 1
        return None

    # --- LÓGICA DO MENU (ESCOLHA/SWITCH) ---
    def visitCmdEscolha(self, ctx):
      
        valor_escolhido = self.visit(ctx.expr(0))
        
        encontrou_caso = False
        
    
        iterator = iter(ctx.children)
        
        try:
            child = next(iterator)
            while child:
                txt = child.getText()
                
                if txt == 'CASO':
                 
                    expr_node = next(iterator)
                    valor_caso = self.visit(expr_node)
                    
                   
                    if valor_escolhido == valor_caso:
                        encontrou_caso = True
                     
                        temp = next(iterator) 
                        
                       
                       
                        temp = next(iterator)
                        while temp.getText() not in ['CASO', 'PADRAO', 'FIM']:
                            if isinstance(temp, MinhaLinguagemParser.ComandoContext):
                                self.visit(temp)
                            temp = next(iterator)
                        return
                        
                elif txt == 'PADRAO':
                    if not encontrou_caso:
                       
                        temp = next(iterator)
                        temp = next(iterator)
                        
                        while temp.getText() != 'FIM':
                            if isinstance(temp, MinhaLinguagemParser.ComandoContext):
                                self.visit(temp)
                            temp = next(iterator)
                        return
                
                child = next(iterator)
        except StopIteration:
            pass
        return None

  
    def visitExprInt(self, ctx):
        return int(ctx.getText())

    def visitExprReal(self, ctx):
        return float(ctx.getText())

    def visitExprBool(self, ctx):
        return ctx.getText() == 'VERDADEIRO'

    def visitExprString(self, ctx):
        # Remove as aspas do texto
        return ctx.getText()[1:-1]

    def visitExprVar(self, ctx):
        nome = ctx.VARIAVEL().getText()
        if nome in self.variaveis:
            return self.variaveis[nome]
        return 0

    def visitExprParentesis(self, ctx):
        return self.visit(ctx.expr())

    def visitExprMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*': return left * right
        return left / right

    def visitExprAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+': return left + right
        return left - right

    def visitExprRelacional(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '>': return left > right
        if op == '>=': return left >= right
        if op == '<': return left < right
        if op == '<=': return left <= right
        if op in ['=', '==']: return left == right
        if op in ['<>', '!=']: return left != right
        return False

    def visitExprE(self, ctx):
        return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

    def visitExprOu(self, ctx):
        return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))