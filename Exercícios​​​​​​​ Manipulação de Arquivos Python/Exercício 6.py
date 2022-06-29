import json

with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

edicao = campeonatus['edicao_atual']
fase = campeonatus['fase_atual']
rodada = campeonatus['rodada_atual']

print(edicao['edicao_id'])
print(fase['_link'])
print(rodada['nome'])
