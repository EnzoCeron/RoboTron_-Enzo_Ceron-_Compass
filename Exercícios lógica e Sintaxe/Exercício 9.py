# crie um programa que recebe 15 valores e armazena em uma lista, e no final da execucao mostre os valores da lista do ultimo para o primeiro

lista = []

# popula a lista
for i in range(0, 15):
    num = int(input("insira um numero: "))
    lista.append(num)

# define o tamanho da lista e a percorre ao contrario printando os items
t = len(lista)
for i in range(t, -1, -1):
    print(lista[i])


