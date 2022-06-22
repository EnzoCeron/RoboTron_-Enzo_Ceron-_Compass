# crie um programa que contem uma funcao que receba dois parametros inteiros e retorna a media dos dois valores

# definindo a funcao
def media():
    a = int(input("Insira um numero: "))
    b = int(input("Insira um numero: "))

    media = (a + b) / 2

    return media


# chamando a funcao
num = media()

print(num)
