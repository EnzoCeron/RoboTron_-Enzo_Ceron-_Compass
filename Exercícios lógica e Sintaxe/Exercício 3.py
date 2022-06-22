# contrua um programa que recebe dois valores, soma esses valores e apresenta se o resultado e par ou impar

from random import randint
# criacao de dois valores aleatorios
val1 = randint(0, 100)
val2 = randint(0, 100)

# codigo caso opite por um input manual dos valores
# val1 = int(input("insira um valor: ")))
# val2 = int(input("insira um valor: ")))

# soma das variaveis
soma = val1 + val2


# impar ou par
if soma % 2 == 0:
    print("O valor da soma dos valores e par")
else:
    print("O valor da soma dos valores e impar")
