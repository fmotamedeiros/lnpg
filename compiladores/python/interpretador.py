from parser import analise_sintatica
from lexer import analise_lexica, tokens_da_linguagem

code = 'A = B + C; C = B; A = B - C;'
tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens)
programa = analise_sintatica(tokens)
print (programa)

for token in programa:
    print(token.interpretar())
