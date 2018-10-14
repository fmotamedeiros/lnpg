import sys
import operator

class Token:
    def interpretar(self):
        return None

class Instrucao (Token):

    def __init__(self, a, b, c, operacao):
        self.x = a
        self.y = b
        self.z = c
        self.operacao = operacao
        self.operacoes = { 
            '+': operator.add, 
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        } 
    
    def executar(self, var):
        #Se é instrução com operação
        if self.z:
            if str.isdigit(self.y):
                if str.isdigit(self.z):
                    #VAR = DIGITO + DIGITO
                    var[self.x] = self.operacoes[self.operacao](int(self.y),int(self.z))
                    return var

                #VAR = DIGITO + VAR
                var[self.x] = self.operacoes[self.operacao](int(self.y),int(var[self.z]))
                return var

            if str.isdigit(self.z):
                #VAR = VAR + DIGITO
                var[self.x] = self.operacoes[self.operacao](int(var[self.y]),int(self.z))
                return var
          
            #VAR = VAR + VAR
            var[self.x] = self.operacoes[self.operacao](int(var[self.y]),int(var[self.z]))
            return var
        
        if str.isdigit(self.y):
            #VAR = DIGITO
            var[self.x] = int(self.y)
            return var
        
        #VAR = VAR
        var[self.x] = var[self.y]
        return var

   
    def __str__(self):
        if self.z:
            return self.x + ' ' + self.y + ' ' + self.z  + ' ' + self.operacao +  ' =' + ';'
        return self.x + ' ' + self.y + ' =' + ';' 

#função responsável por reconhecer as expressões
def instrucao (tokens, pos):

    #instrucao simples A 1 = ; A B =;
    if len(tokens) >= (pos+4):
        if tokens[pos][1] == 'VAR' and (tokens[pos+1][1] == 'VAR' or tokens[pos+1][1]== 'DIGITO') and tokens[pos+2][1] == 'IGUAL' and  tokens[pos+3][1] == 'SEPARADOR':
            #retorna os valores para fora da função
            return ((pos+4), Instrucao(tokens[pos][0], tokens[pos+1][0], None, None))

    #instrucao com operações A B 2 * = ;
    if len(tokens) >= (pos+6):
        if tokens[pos][1] == 'VAR' and (tokens[pos+1][1] == 'VAR' or tokens[pos+1][1] == 'DIGITO') and (tokens[pos+2][1] == 'VAR' or tokens[pos+2][1] == 'DIGITO') and tokens[pos+4][1] == 'IGUAL' and tokens[pos+5][1] == 'SEPARADOR':

            if tokens[pos+3][1] == 'SOMA':
                return ((pos+6), Instrucao(tokens[pos][0], tokens[pos+1][0], tokens[pos+2][0], '+'))

            if tokens[pos+3][1] == 'SUB':
                return ((pos+6), Instrucao(tokens[pos][0], tokens[pos+1][0], tokens[pos+2][0], '-'))

            if tokens[pos+3][1] == 'MULT':
                return ((pos+6), Instrucao(tokens[pos][0], tokens[pos+1][0], tokens[pos+2][0], '*'))

            if tokens[pos+3][1] == 'DIV':
                return ((pos+6), Instrucao(tokens[pos][0], tokens[pos+1][0], tokens[pos+2][0], '/'))

    return (pos, None)

def analise_sintatica(tokens):
    pos = 0
    programa = []
    while pos < len(tokens):
        posAtual, inst = instrucao(tokens, pos)
        if pos != posAtual:
            programa.append(inst)
            pos = posAtual
        else:
            sys.stderr.write('Problema no programa: %s\n' % pos)
            sys.exit(1)
    return programa
