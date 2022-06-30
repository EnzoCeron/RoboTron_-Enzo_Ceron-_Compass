# Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

# importando a biblioteca json
import json

# lendo e guardando o arquivo
with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

# separando em variaveis
edicao = campeonatus['edicao_atual']
fase = campeonatus['fase_atual']
rodada = campeonatus['rodada_atual']

#printando
print(edicao['edicao_id'])
print(fase['_link'])
print(rodada['nome'])
