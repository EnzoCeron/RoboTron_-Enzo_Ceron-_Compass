# Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

# importando a biblioteca json e pprint
import pprint
import json

# lendo e armazenando o arquivo JSON2
with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

# atribuindo variaveis a os dicionarios e printando seus dados
pprint.pprint(campeonatus)
