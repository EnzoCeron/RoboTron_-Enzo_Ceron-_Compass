# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias.
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364.
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# input do usuario
idade = int(input("insira sua idade em dias: "))

# realizacao das contas
a = idade // 365
m = round(idade % 365) // 30
d = round(idade % 365) % 30

# print da variaveis
print(a, "ano(s)")
print(m, "messe(s)")
print(d, "dias(s)")
