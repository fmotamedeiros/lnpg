from sintatico import *
from lexico import *
from configs import *

code = '55 5*A=;'
tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens, '\n')
programa = analise_sintatica(tokens)
#print (programa)

for token in programa:
    print(token.interpretar())


