# construa um progrma que armazena uma idade em uma variavel e compara,
# se a idade for maior que 18, apresenta "Maior de idade",
# se a idade for menor que 12, apresenta "Voce e uma crianca"
# e se for maior que 12 e menor que 18, apresenta "Voce e um adolescente"

from random import randint

# variavel da idade

# variavel automatizada
# idade = randint(0, 99)

# variavel de input do usuario
idade = (int(input("qual sua idade? ")))

# definindo a faixa etaria
if idade >= 18:
    print("Voce e maior de idade")
elif 18 > idade > 12:
    print("Voce e um adolescente")
elif idade <= 12:
    print("Voce e uma crianca")
