from modules.AnaliseLexica import AnaliseLexica

class Lexer:
    def __init__(self):
        self.run()

    def run(self):
        code = 'A = B + C; C = B; A = B - C;'
        tokens = AnaliseLexica().analise_lexica(code)
        print(tokens)

if __name__ == "__main__":
    Lexer()
