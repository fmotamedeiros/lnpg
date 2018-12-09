import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from simbolos import tabela, adicionar, ler

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

class Lista (Construcao):
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, [self.var2, self.var3])

class TamanhoLista (Construcao):
    def __init__(self, var):
        self.var = var

    def interpretar(self):
        print(len(tabela[self.var]))

class Imprimir (Construcao):
    def __init__(self, var):
        self.var = var

    def interpretar(self):
        print(tabela.get(self.var))