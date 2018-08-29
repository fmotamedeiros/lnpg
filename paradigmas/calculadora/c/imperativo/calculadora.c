#include<stdio.h>

int main(){
    int op1 = 0;
    int op2 = 0;

    int operador = 0;

    while (operador != 5){

        printf("(1) Soma\n");
        printf("(2) Subtração\n");
        printf("(3) Multiplicação\n");
        printf("(4) Divisão\n");
        printf("(5) Sair\n");

        printf("Digite a operação desejada: ");
        scanf("%d", &operador);

        if (operador == 5){
            break;
        }

        printf("Digite o primeiro operando: ");
        scanf("%d", &op1);

        printf("Digite o segundo operando: ");
        scanf("%d", &op2);

        int resultado = 0;

        if (operador == 1){
            resultado = op1 + op2;
        }

        if (operador == 2){
            resultado = op1 - op2;
        }

        if (operador == 3){
            resultado = op1 * op2;
        }

        if (operador == 4){
            resultado = op1 / op2;
        }

        printf("%d\n\n", resultado);
    }

    return 1;
}