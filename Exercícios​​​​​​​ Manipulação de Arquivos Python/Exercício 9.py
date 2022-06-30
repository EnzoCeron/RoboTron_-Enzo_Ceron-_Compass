# Usando Pandas, leia apenas os dados da coluna Age do CSV.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel, usando o parametro para selecionar uma coluna especifica
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',', usecols=['Age'])

# printando
print(arquivo)