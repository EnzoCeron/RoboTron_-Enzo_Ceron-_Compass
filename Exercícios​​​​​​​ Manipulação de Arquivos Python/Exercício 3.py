# Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

# importando a variavel JSON
import json

# Lendo e guardando em uma variavel o arquivo JSON1
with open("JSON1.json", encoding="UTF-8") as partida:
    json_partida = json.load(partida)

# atribuindo uma variavel a lista presente no JSON
copa_brasil = json_partida['copa-do-brasil'][0]

# atribuindo a uma variavel cada um dos dados requisitados
placar = copa_brasil['placar']
status = copa_brasil['status']
estadio = copa_brasil['estadio']['nome_popular']

# print das informacoes
print('O estadio que residiu o jogo foi o estadio %s' % estadio)
print('O jogo esta ja esta %s' % status)
print('O placar final foi de %s' % placar)
