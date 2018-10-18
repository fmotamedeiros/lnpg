import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica

class Construcao:
  def interpretar(self):
      return None

class Expressao (Construcao):
    def __init__(self, var1, var2, operador):
        self.var1 = var1
        self.var2 = var2
        self.operador = operador

    def interpretar(self):
        return self.calcular()

    def calcular(self):
        if self.operador == '+':
            return int(self.var1) + int(self.var2)
        elif self.operador == '-':
            return int(self.var1) - int(self.var2)
        elif self.operador == '*':
            return int(self.var1) * int(self.var2)
        elif self.operador == '/':
            return int(self.var1) / int(self.var2)

class ExpressaoAdicional (Construcao):
    def __init__(self, var, resultado, operador):
        self.var = var
        self.operador = operador
        self.resultado = resultado

    def interpretar(self):
        return self.calcular()

    def calcular(self):
        if self.operador == '+':
            return int(self.resultado) + int(self.var)
        elif self.operador == '-':
            return int(self.resultado) - int(self.var)
        elif self.operador == '*':
            return int(self.resultado) * int(self.var)
        elif self.operador == '/':
            return int(self.resultado) / int(self.var)