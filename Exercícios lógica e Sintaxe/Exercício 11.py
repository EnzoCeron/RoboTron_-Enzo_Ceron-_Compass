# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar
# em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
# Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
# Saída: Apresente a duração do jogo conforme exemplo abaixo

# input do usuario
inicio = int(input("insira o horario de inicio: "))
fim = int(input('Insira o horario de termino: '))

# realizacao das contas e prints
if inicio > fim:
    horas = 24 -(inicio - fim)
    print('O total de horas foi de', horas)
elif inicio < fim:
    horas = inicio - fim
    print("O total de horas foi de", horas)
elif inicio == fim:
    print("O jogo durou 24h")


