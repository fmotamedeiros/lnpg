import sys
from lexer import analise_lexica, tokens_da_linguagem
from simbolos import adicionarFuncao

construcoes = [
    (['VAR', 'IGUAL', 'VAR', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'DIGITO', 'SEPARADOR'], 'AtrSimples'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'VAR', 'OPERADOR', 'DIGITO', 'SEPARADOR'], 'Atr'),
    (['VAR', 'IGUAL', 'DIGITO', 'OPERADOR', 'VAR', 'SEPARADOR'], 'Atr'),
    (['IMPRIMIR', 'ABRIR', 'VAR', 'FECHAR', 'SEPARADOR'], 'Imprimir'),
    (['VAR', 'ABRIR', 'FECHAR', 'SEPARADOR'], 'Funcao'),
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
        
        lookAhead = pos + 3
        if lookAhead < len(tokens):
            inicio = pos
            if tokens[lookAhead][1] == 'ABRIR_FUNC':
                termino = lookAhead
                while tokens[termino][1] != 'FECHAR_FUNC':
                    termino = termino + 1
                
                blocos = []         
                pos = pos + 4           
                while pos < termino:
                    posAtual, construcao = consumirTokens(tokens, pos)
                    if pos != posAtual:
                        blocos.append((str(pos) + '-' + str(posAtual-1), construcao))
                        pos = posAtual
                    else:
                        sys.stderr.write('Problema na funcao: %s\n' % pos)
                        sys.exit(1)
                adicionarFuncao(tokens[inicio][0], blocos)
                
                pos = pos + 1
                posAtual = pos

        if pos < len(tokens):
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