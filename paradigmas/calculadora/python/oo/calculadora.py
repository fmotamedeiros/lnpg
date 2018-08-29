class Calculadora:

    def __init__(self, op1, op2, operador):
        self.op1 = op1
        self.op2 = op2
        self.operador = operador
        self.resultado = 0
     
    def calcular(self):
        if self.operador == '+':
            self.resultado = self.soma()
        if self.operador == '-':
            self.resultado = self.subtracao()
        if self.operador == '*':
            self.resultado = self.multiplicacao()
        if self.operador == '/':
            self.resultado = self.divisao()
        print(self.resultado)

    def soma(self):
        return self.op1 + self.op2

    def subtracao(self):
        return self.op1 - self.op2

    def multiplicacao(self):
        return self.op1 * self.op2

    def divisao(self):
        return self.op1 / self.op2