import sys
from configs import *

class Token:
    def interpretar(self):
        return None

class Atribuicao (Token):

    def __init__(self, a, b, c, operacao):
        self.a = a
        self.b = b
        self.c = c
        self.operacao = operacao

    def interpretar(self):
        if self.c:
            return self.b + self.c + self.operacao + self.a + '=' + ';'
        else:
            return self.a + self.b + '=' + ';'
            
def atribuicao (tokens, pos):
    if len(tokens) >= (pos+4):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL' and tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SEPARADOR':
            
            return ((pos+4), Atribuicao(tokens[pos][0], tokens[pos+2][0], None, None))
        
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SOMA' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                    
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '+'))
                
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SUB' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                    
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '-'))
                
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'MUL' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                    
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '*'))

    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                   
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '/'))
    
## VERIFICAÇÃO DE TOKENS DO TIPO A = OPERAÇÃO COM DIGITOS ##

    if len(tokens) >= (pos+4):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL' and tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SEPARADOR':
            
            return ((pos+4), Atribuicao(tokens[pos][0], tokens[pos+2][0], None, None))

    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SOMA' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':

                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '+'))
    
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SUB' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':

                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '-'))
    
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'MUL' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':

                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '*'))

    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':

                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '/'))

## VERIFICAÇÃO DE ENTRADA POSFIXA PARA REALIZAR CÁLCULOS

    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'DIG' and tokens[pos+1][1] == 'DIG':
            if tokens[pos+2][1] == 'SOMA' and tokens[pos+3][1] == 'VAR' and tokens[pos+4][1] == 'IGUAL':
                if tokens[pos+5][1] == 'SEPARADOR':
                    realizarCalculoPosfixa(tokens, pos)
                    return ((pos+6), Atribuicao(tokens[pos+3][0], tokens[pos][0], tokens[pos+1][0], '+'))
    
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'DIG' and tokens[pos+1][1] == 'DIG':
            if tokens[pos+2][1] == 'SUB' and tokens[pos+3][1] == 'VAR' and tokens[pos+4][1] == 'IGUAL':
                if tokens[pos+5][1] == 'SEPARADOR':
                    realizarCalculoPosfixa(tokens,pos)
                    return ((pos+6), Atribuicao(tokens[pos+3][0], tokens[pos][0], tokens[pos+1][0], '-'))
    
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'DIG' and tokens[pos+1][1] == 'DIG':
            if tokens[pos+2][1] == 'MUL' and tokens[pos+3][1] == 'VAR' and tokens[pos+4][1] == 'IGUAL':
                if tokens[pos+5][1] == 'SEPARADOR':
                    realizarCalculoPosfixa(tokens,pos)
                    return ((pos+6), Atribuicao(tokens[pos+3][0], tokens[pos][0], tokens[pos+1][0], '*'))
    
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'DIG' and tokens[pos+1][1] == 'DIG':
            if tokens[pos+2][1] == 'DIV' and tokens[pos+3][1] == 'VAR' and tokens[pos+4][1] == 'IGUAL':
                if tokens[pos+5][1] == 'SEPARADOR':
                    realizarCalculoPosfixa(tokens,pos)
                    return ((pos+6), Atribuicao(tokens[pos+3][0], tokens[pos][0], tokens[pos+1][0], '/'))
    

    return (pos, None)


def analise_sintatica(tokens):
    pos = 0
    programa = []
    while pos < len(tokens):
        posAtual, att = atribuicao(tokens, pos)
        if pos != posAtual:
            programa.append(att)
            pos = posAtual
        else:
            sys.stderr.write('Problema no programa: %s\n' % pos)
            sys.exit(1)
    return programa
