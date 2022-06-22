# importando a biblioteca JSON
import json

# lendo e guardando em uma variavel o arquivo JSON1
with open("JSON1.json", encoding="UTF-8") as partida:
    json_partida = json.load(partida)

# imprimindo variavel
print(json_partida)
