tabela = {}
funcoes = {}

def adicionar(nome, valor):
    tabela[nome] = valor

def ler(nome):
    return tabela[nome]

def adicionarFuncao(nome, comandos):
    funcoes[nome] = comandos

def lerFuncao(nome):
    return funcoes[nome]