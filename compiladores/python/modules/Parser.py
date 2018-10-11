from compiladores.python.modules.ParserUtils import Atribuicao

class Parser:
    def __init__(self):
        pass

    def atribuicao(self, tokens, pos):
        # pos = 0
        if len(tokens) >= (pos + 4):
            if tokens[pos][1] == 'VAR' and tokens[pos + 1][1] == 'IGUAL' and tokens[pos + 2][1] == ('VAR') or \
                    tokens[pos + 2][1] == ('NUM'):
                if tokens[pos + 3][1] == 'SEPARADOR':
                    return ((pos + 4), Atribuicao(tokens[pos][0], tokens[pos + 2][0], None, None))

        print(len(tokens) >= 6)
        if len(tokens) >= (pos + 6):
            print('>6')

        if len(tokens) >= (pos + 6):
            if tokens[pos][1] == 'VAR' and tokens[pos + 1][1] == 'IGUAL':
                if (tokens[pos + 2][1] == 'VAR' and tokens[pos + 3][1] == 'SOMA') and (
                        tokens[pos + 4][1] == 'VAR' or tokens[pos + 4][1] == ('NUM')):
                    if tokens[pos + 5][1] == 'SEPARADOR':
                        return ((pos + 6), Atribuicao(tokens[pos][0], tokens[pos + 2][0], tokens[pos + 4][0], '+'))
        if len(tokens) == (pos + 6):
            if tokens[pos][1] == 'VAR' and tokens[pos + 1][1] == 'IGUAL':
                if (tokens[pos + 2][1] == 'VAR' and tokens[pos + 3][1] == 'SUB') and (
                        tokens[pos + 4][1] == 'VAR' or tokens[pos + 4][1] == ('NUM')):
                    if tokens[pos + 5][1] == 'SEPARADOR':
                        return ((pos + 6), Atribuicao(tokens[pos][0], tokens[pos + 2][0], tokens[pos + 4][0], '-'))
        return (pos, None)

    def analise_sintatica(self, tokens):
        pos = 0
        programa = []
        while pos < len(tokens):
            posAtual, att = self.atribuicao(tokens, pos)
            if pos != posAtual:
                programa.append(att)
                pos = posAtual
            else:
                __import__("sys").stderr.write('Problema no programa: %s\n' % pos)
                __import__("sys").exit(1)
        return programa