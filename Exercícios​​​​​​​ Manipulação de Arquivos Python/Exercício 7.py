# Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

# importando a biblioteca
import json

# lendo e guardando o arquivo em uma variavel
with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

# loop para printar cada item
for item in campeonatus:
    print(campeonatus[item])