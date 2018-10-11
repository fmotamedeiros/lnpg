class AnaliseLexica:
    def __init__(self):
        self.tokens_da_linguagem = [
            (r'[ \t\n]+', None),
            (r'#[^\n]*', None),
            (r'[A|B|C]', 'VAR'),
            (r'[=]', 'IGUAL'),
            (r'[+]', 'SOMA'),
            (r'[-]', 'SUB'),
            (r'[*]', 'MULTIPLICACAO'),
            (r'[/]', 'DIVISAO'),
            (r'[;]', 'SEPARADOR')
        ]

    def analise_lexica(self, programa):
        posicao = 0
        tokens_identificados = []
        while posicao < len(programa):
            match = None
            for token_da_linguagem in self.tokens_da_linguagem:
                padrao, identificador = token_da_linguagem
                regex = __import__("re").compile(padrao)
                match = regex.match(programa, posicao)
                if match:
                    padrao_identificado = match.group(0)
                    if identificador:
                        token = (padrao_identificado, identificador)
                        tokens_identificados.append(token)
                    break
            if not match:
                __import__("sys").stderr.write('Problema no programa: %s\n' % programa[posicao])
                __import__("sys").exit(1)
            else:
                posicao = match.end(0)
        return tokens_identificados