import sys
from lexer import analise_lexica, tokens_da_linguagem
from myparser import analise_sintatica
from simbolos import tabela, adicionar, ler
from ast import *

code = input("Entre com a expressao: ")
tokens = analise_lexica(code, tokens_da_linguagem)

#print('\n')

print(tokens)

#print('\n')

programa = analise_sintatica(tokens)
print (programa)

#print('\n')

for construcao in programa:
    if construcao[1] == 'AtrSimples':
        inicio = int(construcao[0].split('-')[0])
        atrSimples = AtrSimples(tokens[inicio][0], tokens[inicio + 2][0])
        atrSimples.interpretar()
    if construcao[1] == 'AtrRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrRaiz = AtrRaiz(tokens[inicio][0], tokens[inicio + 4][0])
        atrRaiz.interpretar()   
    if construcao[1] == 'AtrFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrFatorial = AtrFatorial(tokens[inicio][0], tokens[inicio + 4][0])
        atrFatorial.interpretar()  
    if construcao[1] == 'AtrPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrPotencia = AtrPotencia(tokens[inicio][0], tokens[inicio + 4][0], tokens[inicio + 6][0])
        atrPotencia.interpretar()    
    if construcao[1] == 'AtrRandom':
        inicio = int(construcao[0].split('-')[0])
        atrRandom = AtrRandom(tokens[inicio][0], tokens[inicio + 4][0], tokens[inicio + 6][0])
        atrRandom.interpretar()            
    if construcao[1] == 'Atr':
        inicio = int(construcao[0].split('-')[0])
        atr = Atr(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 3][0]
        )
        atr.interpretar()

    if construcao[1] == 'AtrDigitoRaiz' or construcao[1] == 'AtrVarRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrDigitoRaiz = AtrDigitoRaiz(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 3][0]
        )
        atrDigitoRaiz.interpretar()
    if construcao[1] == 'AtrDigitoFatorial' or construcao[1] == 'AtrVarFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrDigitoFatorial = AtrDigitoFatorial(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 3][0]
        )
        atrDigitoFatorial.interpretar()
    if construcao[1] == 'AtrDigitoPotencia' or construcao[1] == 'AtrVarPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrDigitoPotencia = AtrDigitoPotencia(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 8][0],
            tokens[inicio + 3][0]
        )
        atrDigitoPotencia.interpretar()
    if construcao[1] == 'AtrDigitoRandom' or construcao[1] == 'AtrVarRandom':
        inicio = int(construcao[0].split('-')[0])
        atrDigitoRandom = AtrDigitoRandom(
            tokens[inicio][0], 
            tokens[inicio + 2][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0], 
            tokens[inicio + 3][0]
        )
        atrDigitoRandom.interpretar()
    if construcao[1] == 'AtrRaizDigito' or construcao[1] == 'AtrRaizVar':
        inicio = int(construcao[0].split('-')[0])
        atrRaizDigito = AtrDigitoRaiz(
            tokens[inicio][0], 
            tokens[inicio + 7][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0]
        )
        atrRaizDigito.interpretar()
    if construcao[1] == 'AtrRaizRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrRaizRaiz = AtrRaizRaiz(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 6][0]
        )
        atrRaizRaiz.interpretar()
    if construcao[1] == 'AtrRaizFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrRaizFatorial = AtrRaizFatorial(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 6][0]
        )
        atrRaizFatorial.interpretar()    
    if construcao[1] == 'AtrRaizPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrRaizPotencia = AtrRaizPotencia(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 6][0]
        )
        atrRaizPotencia.interpretar()
    if construcao[1] == 'AtrRaizRandom':
        inicio = int(construcao[0].split('-')[0])
        atrRaizRandom = AtrRaizRandom(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 6][0]
        )
        atrRaizRandom.interpretar()
    if construcao[1] == 'AtrFatorialDigito' or construcao[1] == 'AtrFatorialVar':
        inicio = int(construcao[0].split('-')[0])
        atrFatorialDigito = AtrDigitoFatorial(
            tokens[inicio][0], 
            tokens[inicio + 7][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0]
        )
        atrFatorialDigito.interpretar()
    if construcao[1] == 'AtrFatorialRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrFatorialRaiz = AtrRaizFatorial(
            tokens[inicio][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0]
        )
        atrFatorialRaiz.interpretar()
    if construcao[1] == 'AtrFatorialFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrFatorialFatorial = AtrFatorialFatorial(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 6][0]
        )
        atrFatorialFatorial.interpretar()
    if construcao[1] == 'AtrFatorialPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrFatorialPotencia = AtrFatorialPotencia(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 6][0]
        )
        atrFatorialPotencia.interpretar()
    if construcao[1] == 'AtrFatorialRandom':
        inicio = int(construcao[0].split('-')[0])
        atrFatorialRandom = AtrFatorialRandom(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 6][0]
        )
        atrFatorialRandom.interpretar()
    if construcao[1] == 'AtrPotenciaDigito' or construcao[1] == 'AtrPotenciaVar':
        inicio = int(construcao[0].split('-')[0])
        atrPotenciaDigito = AtrDigitoPotencia(
            tokens[inicio][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrPotenciaDigito.interpretar()
    if construcao[1] == 'AtrPotenciaRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrPotenciaRaiz = AtrRaizPotencia(
            tokens[inicio][0], 
            tokens[inicio + 11][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrPotenciaRaiz.interpretar()    
    if construcao[1] == 'AtrPotenciaFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrPotenciaFatorial = AtrFatorialPotencia(
            tokens[inicio][0], 
            tokens[inicio + 11][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrPotenciaFatorial.interpretar()
    if construcao[1] == 'AtrPotenciaPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrPotenciaPotencia = AtrPotenciaPotencia(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 13][0],
            tokens[inicio + 8][0]
        )
        atrPotenciaPotencia.interpretar()
    if construcao[1] == 'AtrPotenciaRandom':
        inicio = int(construcao[0].split('-')[0])
        atrPotenciaRandom = AtrPotenciaRandom(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 13][0],
            tokens[inicio + 8][0]
        )
        atrPotenciaRandom.interpretar()
    if construcao[1] == 'AtrRandomDigito' or construcao[1] == 'AtrRandomVar':
        inicio = int(construcao[0].split('-')[0])
        atrRandomDigito = AtrDigitoRandom(
            tokens[inicio][0], 
            tokens[inicio + 9][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrRandomDigito.interpretar()
    if construcao[1] == 'AtrRandomRaiz':
        inicio = int(construcao[0].split('-')[0])
        atrRandomRaiz = AtrRaizRandom(
            tokens[inicio][0], 
            tokens[inicio + 11][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrRandomRaiz.interpretar()
    if construcao[1] == 'AtrRandomFatorial':
        inicio = int(construcao[0].split('-')[0])
        atrRandomFatorial = AtrFatorialRandom(
            tokens[inicio][0], 
            tokens[inicio + 11][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrRandomFatorial.interpretar()
    if construcao[1] == 'AtrRandomPotencia':
        inicio = int(construcao[0].split('-')[0])
        atrRandomPotencia = AtrPotenciaRandom(
            tokens[inicio][0], 
            tokens[inicio + 11][0], 
            tokens[inicio + 13][0], 
            tokens[inicio + 4][0],
            tokens[inicio + 6][0],
            tokens[inicio + 8][0]
        )
        atrRandomPotencia.interpretar()
    if construcao[1] == 'AtrRandomRandom':
        inicio = int(construcao[0].split('-')[0])
        atrRandomRandom = AtrRandomRandom(
            tokens[inicio][0], 
            tokens[inicio + 4][0], 
            tokens[inicio + 6][0], 
            tokens[inicio + 11][0],
            tokens[inicio + 13][0],
            tokens[inicio + 8][0]
        )
        atrRandomRandom.interpretar()

    if construcao[1] == 'Imprimir':
        inicio = int(construcao[0].split('-')[0])
        imprimir = Imprimir(
            tokens[inicio + 2][0]
        )
        imprimir.interpretar()