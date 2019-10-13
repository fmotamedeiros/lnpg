import sys
from sintatico import *
tokens_da_linguagem = [
    (r'[ \t\n]+', None),
    (r'#[^\n]*', None),
    (r'[A|B|C]', 'VAR'),
    (r'[0-9]+', 'DIG'),
    (r'[=]', 'IGUAL'),
    (r'[+]', 'SOMA'),
    (r'[-]', 'SUB'),
    (r'[/]', 'DIV'),
    (r'[*]', 'MUL'),
    (r'[;]', 'SEPARADOR')
]

def realizarCalculoPosfixa(tokens, pos):
        if tokens[pos+2][1] == 'SOMA':
            b = int(tokens[pos][0])
            c = int(tokens[pos+1][0])
            resultado = ('A = {}'.format((b+c)))
            return print(resultado)
        elif tokens[pos+2][1] == 'SUB':
            b = int(tokens[pos][0])
            c = int(tokens[pos+1][0])
            resultado = ('A = {}'.format((b-c)))
            return print(resultado)
        elif tokens[pos+2][1] == 'MUL':
            b = int(tokens[pos][0])
            c = int(tokens[pos+1][0])
            resultado = ('A = {}'.format((b*c)))
            return print(resultado)
        elif tokens[pos+2][1] == 'DIV':
            b = float(tokens[pos][0])
            c = float(tokens[pos+1][0])
            resultado = ('A = {}'.format((b/c)))
            return print(resultado)
