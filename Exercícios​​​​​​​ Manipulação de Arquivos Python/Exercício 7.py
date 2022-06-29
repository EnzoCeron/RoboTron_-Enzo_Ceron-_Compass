import json

with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

for item in campeonatus:
    print(campeonatus[item])