from parserr import analise_sintatica
from parserr import Atribuicao
from lexer import analise_lexica, tokens_da_linguagem

code = 'A = 3+2;'
print('\n')
tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens, '\n')

programa = analise_sintatica(tokens)
print (programa)
print('\n')

for token in programa:
    print(token.interpretar())

print('\n' + 'O resultado das expressoes sao:')
for token in programa:
    if(token.calcular() == None):
        print('Nao ha operacao a fazer')
    else:
        print(token.calcular())




