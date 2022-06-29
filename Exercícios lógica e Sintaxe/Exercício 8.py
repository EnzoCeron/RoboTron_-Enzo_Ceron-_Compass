# crie um programa que le um valor inteiro para X. Se o valor for par calcular o fatorial de x em uma funcao
# e apresentar o resultado fora da funcao. se o valor for impar, apresentar uma funcao a tabuada
# de 1 a 10 de X.

# definindo funcao do fatorial
def fatorial(num):

    resultado=1

    for n in range(1,num+1):
        resultado *= n

    return resultado

# definindo funcao que printa a tubuada
def tabuada(num):

    for n in range(1,11):
        resultado = n * num
        print(n, 'x', num, '=', resultado)
    return " "


# input do usuario
numero = int(input("Insira um numero: ") )

# define se o numero e impar ou par e realiza a funcao definida
if numero % 2 == 0:
    fator = fatorial(numero)
    print(fator)
else:
    print(tabuada(numero))
