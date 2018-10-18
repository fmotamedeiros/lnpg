import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from ast import *

code = '1 + 3 + 5 - 8'
tokens = analise_lexica(code, tokens_da_linguagem)

print(tokens)

programa = analise_sintatica(tokens)
print (programa)

resultado = 0

for construcao in programa:
    if construcao[1] == 'Expressao':
        inicio = int(construcao[0][0])
        expressao = Expressao(tokens[inicio][0], tokens[inicio + 2][0], tokens[inicio + 1][0])
        resultado = expressao.interpretar()
    if construcao[1] == 'ExpressaoAdicional':
        inicio = int(construcao[0][0])
        expressaoAdicional = ExpressaoAdicional(tokens[inicio + 1][0], resultado, tokens[inicio][0])
        resultado = expressaoAdicional.interpretar()
    
print(resultado)
