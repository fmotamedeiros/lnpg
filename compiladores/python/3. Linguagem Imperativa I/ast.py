import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from simbolos import tabela, adicionar, ler, adicionarFuncao, lerFuncao

class Construcao:
  def interpretar(self):
      return None

class AtrSimples (Construcao):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:
            adicionar(self.var1, self.var2)

class Atr (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):
        if self.operador == '+':
            return int(self.var2) + int(self.var3)
        elif self.operador == '-':
            return int(self.var2) - int(self.var3)
        elif self.operador == '*':
            return int(self.var2) * int(self.var3)
        elif self.operador == '/':
            return int(self.var2) / int(self.var3)

class Imprimir (Construcao):
    def __init__(self, var):
        self.var = var

    def interpretar(self):
        print(tabela.get(self.var))

class Funcao (Construcao):
    def __init__(self, nome, tokens):
        self.nome = nome
        self.tokens = tokens

    def interpretar(self):
        comandos = lerFuncao(self.nome)
        consts = instaciarConstrucoes(comandos, self.tokens)
        for const in consts:
            const.interpretar()

def instaciarConstrucoes(infoConstrucoes, tokens):
    lstConstrucoes = []
    for construcao in infoConstrucoes:
        if construcao[1] == 'AtrSimples':
            inicio = int(construcao[0].split('-')[0])
            atrSimples = AtrSimples(tokens[inicio][0], tokens[inicio + 2][0])
            lstConstrucoes.append(atrSimples)
        if construcao[1] == 'Atr':
            inicio = int(construcao[0].split('-')[0])
            atr = Atr(
                tokens[inicio][0], 
                tokens[inicio + 2][0], 
                tokens[inicio + 4][0], 
                tokens[inicio + 3][0]
            )
            lstConstrucoes.append(atr)
        if construcao[1] == 'Imprimir':
            inicio = int(construcao[0].split('-')[0])
            imprimir = Imprimir(
                tokens[inicio + 2][0]
            )
            lstConstrucoes.append(imprimir)
        if construcao[1] == 'Funcao':
            inicio = int(construcao[0].split('-')[0])
            funcao = Funcao(tokens[inicio][0], tokens)
            lstConstrucoes.append(funcao)
    return lstConstrucoes