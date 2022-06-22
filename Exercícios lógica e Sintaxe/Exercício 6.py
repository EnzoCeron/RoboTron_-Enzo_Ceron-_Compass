# Construa um programa que receba um valor inteiro maior que 2 em uma variavel X e apresenta os impares entre 0 e X

# declaracao de variaveis
num = int
valida = False
impares = []

# validacao se o numero e maior do que 2
while not valida:
    num = int(input("Insira um numero: "))
    if num <= 2:
        print("insira um valor maior")
        continue
    else:
        valida = True

# selecao dos numeros impares no intervalo
for i in range(0, num):
    if i % 2 == 1:
        impares.append(i)

# print
print(impares)