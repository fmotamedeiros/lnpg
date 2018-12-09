tabela = {}

def adicionar(nome, valor):
    tabela[nome] = valor

def tamanho(nome):
    return len(tabela[nome])

def ler(nome):
    return tabela[nome]