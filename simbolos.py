tabela = {}

def adicionar(nome, valor):
    tabela[nome] = valor

def tamanho(nome):
    return len(tabela[nome])

def remover(nome, valor):
    listaAntiga = tabela[nome]
    listaAntiga.remove(valor)

def ler(nome):
    return tabela[nome]