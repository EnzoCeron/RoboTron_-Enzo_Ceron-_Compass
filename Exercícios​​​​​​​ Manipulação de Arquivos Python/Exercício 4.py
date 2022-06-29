#No JSON 1 printe todas as chaves e valores do time visitante

# importando a variavel JSON
import json

# Lendo e guardando em uma variavel o arquivo JSON1
with open("JSON1.json", encoding="UTF-8") as partida:
    json_partida = json.load(partida)

# atribuindo uma variavel ao dicionario time_visitante
copa_brasil = json_partida['copa-do-brasil'][0]
visitante = copa_brasil['time_visitante']

# atribuindo variaveis a cada valor do diconario do time visitante
id = visitante["time_id"]
nome = visitante["nome_popular"]
sigla = visitante["sigla"]
escudo = visitante["escudo"]

# print em formato de dicionario
# print(visitante)

# print formatado
for i in visitante:
    if i == 'time_id':
        print(i, ':', id)
    elif i == 'nome_popular':
        print(i, ':', nome)
    elif i == 'sigla':
        print(i, ':', sigla)
    elif i == 'escudo':
        print(i, ':', escudo)
