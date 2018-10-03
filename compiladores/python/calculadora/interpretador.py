from calculadora import calcular #arquivo novo feito a funcao calcular
from lexer import analise_lexica, tokens_da_linguagem #importando a função e a lista feita

expressao = '30 50 -' #expressão mat já feita em pós-fixa!
tokens = analise_lexica(expressao, tokens_da_linguagem) #usando a expressão acima
print(tokens) #conseguidos pelo arquivo analisador 'lexer'
resultado = calcular(tokens) #chama a função calcular usando o resultado da análise léxica
print (resultado)