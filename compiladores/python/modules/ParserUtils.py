class Token:
    def interpretar(self):
        return None

class Atribuicao (Token):
    def __init__(self, a, b, c, operacao):
        self.a = a
        self.b = b
        self.c = c
        self.operacao = operacao

    def interpretar(self):
        if self.c:
            return self.a + ' = ' + self.b + self.operacao + self.c + ';'
        return self.a + ' = ' + self.b + ';'