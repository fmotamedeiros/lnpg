import sys
from lexer import analise_lexica, tokens_da_linguagem

construcoes = [
    (['VAR', 'IGUAL', 'VAR', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'DIGITO', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['IMPRIMIR', 'ABRIR', 'VAR', 'FECHAR', 'SEPARADOR'], 'Imprimir'),
    (['VAR', 'IGUAL', 'ABRELISTA', 'DIGITO', 'SEPARALISTA', 'DIGITO', 'FECHALISTA', 'SEPARADOR'], 'Lista'),
    (['TAMANHO', 'ABRIR', 'VAR', 'FECHAR', 'SEPARADOR'], 'Tamanho')
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

#code = 'A = 10; imprimir(A);'
#tokens = analise_lexica(code, tokens_da_linguagem)

#print(tokens)

#programa = analise_sintatica(tokens)
#print (programa)

#for attr in programa:
#    print(attr)