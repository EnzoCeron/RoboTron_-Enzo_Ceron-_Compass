# Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores,
# ["maça", "banana", "pera"]

# populando a lista
lista = []
lista_frutas = ["maçã", "banana", "pera"]
for i in range(0, 3):
    fruta = input("insira ume fruta: ")
    lista.append(fruta)

# comparando as listas
for item in lista:
    for fruta in lista_frutas:
        if item == fruta:
            print('O item', item, 'esta contido na lista de frutas')
    if item not in lista_frutas:
        print("o item nao esta na lista de frutas")
