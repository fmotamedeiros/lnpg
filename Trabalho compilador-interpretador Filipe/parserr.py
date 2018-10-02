import sys

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
            return self.a + ' = ' + self.b + self.c + self.operacao + ';'
        return self.a + ' = ' + self.b + ';' 
    
    def calcular(self):
        if self.c:
            if(self.operacao == '+'):
                calculo = int(self.b) + int(self.c)
                return self.a + ' = ' + str(calculo)
            elif(self.operacao == '-'):
                calculo = int(self.b) - int(self.c)
                return self.a + ' = ' + str(calculo)
            elif(self.operacao == '*'):
                calculo = int(self.b) * int(self.c)
                return self.a + ' = ' + str(calculo)
            elif(self.operacao == '/'):
                calculo = int(self.b) / int(self.c)
                return self.a + ' = ' + str(calculo)

def atribuicao (tokens, pos): #VARIAVEL + VARIAVEL 
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
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'MULT' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '*'))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'VAR':
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '/'))
    if len(tokens) >= (pos+4): #DIG + DIG
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
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'MULT' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '*'))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'DIG':
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '/'))    
    if len(tokens) >= (pos+4): #VARIAVEL+DIG
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL' and tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SEPARADOR':
            return ((pos+4), Atribuicao(tokens[pos][0], tokens[pos+2][0], None, None))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if ((tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SOMA' and tokens[pos+4][1] == 'DIG') | (tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SOMA' and tokens[pos+4][1] == 'VAR')):
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '+'))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if ((tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SUB' and tokens[pos+4][1] == 'DIG') | (tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'SUB' and tokens[pos+4][1] == 'VAR')):
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '-'))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if ((tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'MULT' and tokens[pos+4][1] == 'DIG') | (tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'MULT' and tokens[pos+4][1] == 'VAR')):
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '*'))
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
            if ((tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'DIG') | (tokens[pos+2][1] == 'DIG' and tokens[pos+3][1] == 'DIV' and tokens[pos+4][1] == 'VAR')):
                if tokens[pos+5][1] == 'SEPARADOR':
                    return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], '/'))
    return (pos, None)

def analise_sintatica (tokens):
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