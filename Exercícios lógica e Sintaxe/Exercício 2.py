# construa um programa que armazena em duas variaveis duas notas e apresenta a media entra as duas

from random import randint
# criacao de codigo para armazenar duas notas, que no caso serao geradas automaticamente

nota1 = randint(0, 10)
nota2 = randint(0, 10)

# codigo caso queira  as notas por input do usuario
# nota1 = int(input("insira uma nota: ")))
# nota2 = int(input("insira uma nota: ")))

# media das notas
media = (nota1 + nota2) / 2

#print
print(nota1)
print(nota2)
print(media)

