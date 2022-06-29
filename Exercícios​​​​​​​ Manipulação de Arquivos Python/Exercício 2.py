#Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal

# importando a variavel JSON
import json

# Lendo e guardando em uma variavel o arquivo JSON1
with open("JSON1.json", encoding="UTF-8") as partida:
    json_partida = json.load(partida)

# atribuindo uma variavel ao dicionario time_mandante
copa_brasil = json_partida['copa-do-brasil'][0]['time_mandante']

# referenciando o nome do time dentro da variavel
vencedor = copa_brasil['nome_popular']

# imprimindo o nome do time vencedor
print("O time vencedor foi", vencedor)
