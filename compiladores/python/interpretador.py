from parser import *
from lexer import *

code = 'A = B + C; C = B; A = B - C;'
tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens)
programa = analise_sintatica(tokens)
print (programa)

for token in programa:
    print(token.interpretar())
