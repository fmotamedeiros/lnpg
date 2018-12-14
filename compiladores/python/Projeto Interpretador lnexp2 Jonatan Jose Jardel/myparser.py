import sys
from lexer import analise_lexica, tokens_da_linguagem

construcoes = [
    (['VAR', 'IGUAL', 'VAR', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'DIGITO', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRaiz'),
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrFatorial'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrPotencia'),
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRandom'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrVarRaiz'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrVarFatorial'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrVarPotencia'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrVarRandom'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrDigitoRaiz'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrDigitoFatorial'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrDigitoPotencia'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrDigitoRandom'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'AtrRaizVar'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'AtrRaizDigito'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRaizRaiz'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRaizFatorial'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRaizPotencia'),
    (['VAR', 'IGUAL', 'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRaizRandom'),
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'AtrFatorialVar'), 
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'AtrFatorialDigito'), 
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrFatorialFatorial'),
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrFatorialPotencia'),
    (['VAR', 'IGUAL', 'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrFatorialRandom'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'AtrPotenciaVar'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'AtrPotenciaDigito'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrPotenciaRaiz'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrPotenciaFatorial'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrPotenciaPotencia'),
    (['VAR', 'IGUAL', 'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrPotenciaRandom'),
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'VAR', 'SEPARADOR'], 'AtrRandomVar'),    
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'DIGITO', 'SEPARADOR'], 'AtrRandomDigito'),    
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'RAIZ', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRandomRaiz'),
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR',
      'FATORIAL', 'ABRIR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRandomFatorial'),
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'POTENCIA', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRandomPotencia'),
    (['VAR', 'IGUAL', 'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'OPERADOR', 
      'RANDOM', 'ABRIR', 'DIGITO', 'SEPARADOR', 'DIGITO', 'FECHAR', 'SEPARADOR'], 'AtrRandomRandom'), 
    (['IMPRIMIR', 'ABRIR', 'VAR', 'FECHAR', 'SEPARADOR'], 'Imprimir')
]

def consumirTokens(tokens, pos):
    indice = pos
    for construcao in construcoes:
        for token in construcao[0]:
            if token != tokens[indice][1]:
                indice = pos
                break
            else:
                indice = indice + 1
        if indice != pos:
            return (indice, construcao[1])
    return (pos, None)

def analise_sintatica(tokens):
    pos = 0
    programa = []
    while pos < len(tokens):
        posAtual, construcao = consumirTokens(tokens, pos)
        if pos != posAtual:
            programa.append((str(pos) + '-' + str(posAtual-1), construcao))
            pos = posAtual
        else:
            sys.stderr.write('Problema no programa: %s\n' % pos)
            sys.exit(1)
    return programa