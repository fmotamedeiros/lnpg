from compiladores.python.modules.Parser import Parser
from compiladores.python.modules.AnaliseLexica import AnaliseLexica

class Interpretador:
    def __init__(self):
        self.analiseLexica = AnaliseLexica()
        self.parser = Parser()
        self.run()

    def run(self):
        tokens = self.analiseLexica.analise_lexica('A = B + C; C = B; A = B - C;')
        print(tokens)
        programa = self.parser.analise_sintatica(tokens)
        print (programa)
        for token in programa:
            print(token.interpretar())

if __name__ == "__main__":
    Interpretador()