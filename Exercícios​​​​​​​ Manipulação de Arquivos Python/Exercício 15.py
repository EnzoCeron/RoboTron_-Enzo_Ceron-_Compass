# Mostre todos os filmes menos o “The Revenant”.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel, usando o parametro para selecionar uma coluna especifica
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',', usecols=["Movie"])

# comando para printar todas as linhas menos a que possuir o "valor" selecionado
print(arquivo[arquivo["Movie"] != "The Revenant"])