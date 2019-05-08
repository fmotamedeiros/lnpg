from myparser import *
from lexer import *

code = 'A = 19 * 9; '

tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens,'\n')

programa = analise_sintatica(tokens)

print(programa)

for token in programa:
    print(token.compilar())

