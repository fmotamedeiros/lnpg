import sys
import re

tokens_da_linguagem = [
    (r'[ \t\n]+', None),
    (r'#[^\n]*', None),    
    (r'[i][m][p][r][i][m][i][r]', 'IMPRIMIR'),    
    (r'[r][a][i][z]', 'RAIZ'),
    (r'[f][a][t][o][r][i][a][l]', 'FATORIAL'),
    (r'[p][o][t][e][n][c][i][a]', 'POTENCIA'),
    (r'[r][a][n][d][o][m]', 'RANDOM'),
    (r'[A-Za-z]+', 'VAR'),    
    (r'[0-9]{0,15}[,]{0,1}[0-9]{0,4}[0-9]+', 'DIGITO'),    
    (r'[=]', 'IGUAL'),
    (r'[\+\-\*\/]', 'OPERADOR'),
    (r'[;]', 'SEPARADOR'),
    (r'[(]', 'ABRIR'),
    (r'[)]', 'FECHAR'),
]

def analise_lexica(programa, tokens_da_linguagem):
    posicao = 0
    tokens_identificados = []
    while posicao < len(programa):
        match = None
        for token_da_linguagem in tokens_da_linguagem:
            padrao, identificador = token_da_linguagem
            regex = re.compile(padrao)
            match = regex.match(programa, posicao)
            if match:
                padrao_identificado = match.group(0)
                if identificador:
                    token = (padrao_identificado, identificador)
                    tokens_identificados.append(token)
                break
        if not match:
            sys.stderr.write('Problema no programa: %s\n' % programa[posicao])
            sys.exit(1)
        else:
            posicao = match.end(0)
    return tokens_identificados