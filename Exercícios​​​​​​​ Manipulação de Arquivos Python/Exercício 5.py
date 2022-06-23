# importando a biblioteca json
import json

# lendo e armazenando o arquivo JSON2
with open("JSON2.json", encoding="UTF-8") as campeonato:
    campeonatus = json.load(campeonato)

# atribuindo variaveis a os dicionarios e printando seus dados
print(type(campeonatus))
print(campeonatus)
print(campeonatus['campeonato_id'])
print(campeonatus['nome'])
print(campeonatus['slug'])
print(campeonatus['nome_popular'])
atual = campeonatus['edicao_atual']
print(atual['edicao_id'])
print(atual['temporada'])
print(atual['nome'])
print(atual['nome_popular'])
print(atual['slug'])
fase = campeonatus['fase_atual']
print(fase['fase_id'])
print(fase['nome'])
print(fase['slug'])
print(fase['tipo'])
print(fase['_link'])
rodada = campeonatus['rodada_atual']
print(rodada['nome'])
print(rodada['slug'])
print(rodada['rodada'])
print(rodada['status'])
print(campeonatus['status'])
print(campeonatus['tipo'])
print(campeonatus['logo'])
print(campeonatus['regiao'])
fases = campeonatus['fases'][0]
print(fases['fase_id'])
fase104 = fases['edicao']
print(fase104['edicao_id'])
print(fase104['temporada'])
print(fase104['nome'])
print(fase104['nome_popular'])
print(fase104['slug'])
print(fases['nome'])
print(fases['slug'])
print(fases['status'])
print(fases['decisivo'])
print(fases['eliminatorio'])
print(fases['ida_e_volta'])
print(fases['tipo'])
print(fases['grupos'])
print(fases['chaves'])
print(fases['rodadas'])
print(fases['proxima_fase'])
print(fases['fase_anterior'])
print(fases['_link'])
