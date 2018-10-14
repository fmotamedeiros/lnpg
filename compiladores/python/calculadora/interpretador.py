from lexer import analise_lexica, tokens_da_linguagem
from parser import analise_sintatica

expressao = 'A 1 =;B2=;C3=;A 210 30 +=;C A B +=;BC=;AB2/=;'
tokens = analise_lexica(expressao, tokens_da_linguagem)
print(tokens)
programa = analise_sintatica(tokens)
print(programa)
var = {
    'A':0,
    'B':0,
    'C':0
}

for inst in programa:
    print(var)
    var = inst.executar(var)

print(var)
