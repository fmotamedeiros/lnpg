tabela = {}

def adicionar(nome, valor):
    tabela[nome] = valor

def tamanho(nome):
    return len(tabela[nome])

def remover(nome, valor):
    tabela[nome].remove(valor)

def ler(nome):
    return tabela[nome]