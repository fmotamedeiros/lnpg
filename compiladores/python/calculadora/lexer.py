import sys
import re

tokens_da_linguagem = [
    (r'[ \t\n]+', None),
    (r'#[^\n]*', None),
    (r'[+]', 'SOMA'),
    (r'[-]', 'SUB'),
    (r'[*]', 'MULT'),
    (r'[/]', 'DIVI'),
    (r'[0-9]+', 'DÍGITO')
]#EXPRESSÕES REGULARES acima!!!! Não precisa de separador porque só vamos usar uma expressão por vez. 

def analise_lexica(programa, tokens_da_linguagem): #1a variável for 'programa', a segunda vai receber token_da_liguagem
    posicao = 0 #contador
    tokens_identificados = [] #cria lista vazia
    while posicao < len(programa): #"programa" aqui é a entrada lá no main, no caso será len para "expressao"
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


#code = 'A = B + C; C = B; A = B - C;'
#tokens = analise_lexica(code, tokens_da_linguagem)
#print(tokens)