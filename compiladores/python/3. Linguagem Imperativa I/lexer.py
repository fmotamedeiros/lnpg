import sys
import re

tokens_da_linguagem = [
    (r'[ \t\n]+', None),
    (r'#[^\n]*', None),
    (r'[i][m][p][r][i][m][i][r]', 'IMPRIMIR'),
    (r'[A-Za-z]+', 'VAR'),
    (r'[0-9]+', 'DIGITO'),
    (r'[=]', 'IGUAL'),
    (r'[\+\-\*\/]', 'OPERADOR'),
    (r'[;]', 'SEPARADOR'),
    (r'[(]', 'ABRIR'),
    (r'[)]', 'FECHAR'),
    (r'[,]', 'VIRGULA'),
    (r'[{]', 'ABRIR_FUNC'),
    (r'[}]', 'FECHAR_FUNC'),
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


#code = 'A = B / C;'
#tokens = analise_lexica(code, tokens_da_linguagem)
#print(tokens)