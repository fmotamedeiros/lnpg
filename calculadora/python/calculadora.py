import funcionalidades
import menu

operador = 0

while operador != 5:

    menu.imprimeMenu()
    operador = int(input('Qual a operacao desejada: '))

    if operador != 5:

        op1 = int(input('Digite o primeiro operando: '))
        op2 = int(input('Digite o segundo operando: '))

        if operador == 1:
            print('Resultado: ' + funcionalidades.soma(op1, op2))

        if operador == 2:
            print('Resultado: ' + funcionalidades.subtracao(op1, op2))
        
        if operador == 3:
            print('Resultado: ' + funcionalidades.multiplicacao(op1, op2))

        if operador == 4:
            print('Resultado: ' + funcionalidades.divisao(op1, op2))