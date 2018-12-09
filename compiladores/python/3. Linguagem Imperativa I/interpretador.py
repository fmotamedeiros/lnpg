import sys
from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica
from simbolos import tabela, adicionar, ler
from ast import Atr, AtrSimples, Imprimir, Funcao, instaciarConstrucoes

code = 'B = 10; test(){ A = B + 10; B = A; } test(); test(); imprimir(A);'
tokens = analise_lexica(code, tokens_da_linguagem)

print(tokens)

programa = analise_sintatica(tokens)
print (programa)

instanciasContrucoes = instaciarConstrucoes(programa, tokens)
for insConst in instanciasContrucoes:
    insConst.interpretar()
