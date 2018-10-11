from parser import Parser
from lexer import Lexer

class Interpretador:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.run()

    def run(self):
        code = 'A = B + C; C = B; A = B - C;'
        tokens = self.lexer.analise_lexica(code, Lexer().tokens_da_linguagem)
        print(tokens)
        programa = self.parser.analise_sintatica(tokens)
        print (programa)
        for token in programa:
            print(token.interpretar())

if __name__ == "__main__":
    Interpretador()