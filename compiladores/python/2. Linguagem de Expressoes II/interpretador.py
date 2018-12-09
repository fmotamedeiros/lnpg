import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from simbolos import tabela, adicionar, ler
from ast import *

#code = 'A = 10; B = A + 2; imprimir(A); imprimir(B);'
code = 'A = {3, 1}; B = {5, 2}; imprimir(A); tamanho(B);'
tokens = analise_lexica(code, tokens_da_linguagem)

print('\n\n\n')

print(tokens)

print('\n\n\n')

programa = analise_sintatica(tokens)
print (programa)

print('\n\n\n')

for construcao in programa:
    if construcao[1] == 'AtrSimples':
        inicio = int(construcao[0].split('-')[0])
        atrSimples = AtrSimples(tokens[inicio][0], tokens[inicio + 2][0])
        atrSimples.interpretar()
    if construcao[1] == 'Atr':
        inicio = int(construcao[0].split('-')[0])
        atr = Atr(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 3][0]
        )
        atr.interpretar()
    if construcao[1] == 'Lista':
        inicio = int(construcao[0].split('-')[0])
        lista = Lista(tokens[inicio][0], tokens[inicio + 3][0], tokens[inicio + 5][0])
        lista.interpretar()
    if construcao[1] == 'Tamanho':
        inicio = int(construcao[0].split('-')[0])
        lista = TamanhoLista(tokens[inicio + 2][0])
        lista.interpretar()
    if construcao[1] == 'Imprimir':
        inicio = int(construcao[0].split('-')[0])
        imprimir = Imprimir(
            tokens[inicio + 2][0]
        )
        imprimir.interpretar()

