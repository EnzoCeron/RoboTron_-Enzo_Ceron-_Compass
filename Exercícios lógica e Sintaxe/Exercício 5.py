# Construa um programa que recebe 20 valores para X e no final apresenta a media aritimetica dos valores digitados

# variavel de count
soma = 0

# Loop para insercao dos valores e soma de todos
for i in range(0, 20):
    num = int(input("Insira um numero: "))
    soma += num

# media e print final
media = soma / 20
print(media)
