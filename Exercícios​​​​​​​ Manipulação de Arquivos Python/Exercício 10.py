# Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel, usando o parametro para selecionar uma coluna especifica
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',', usecols=['Movie'])

# printando uma linha específica do arquivo
print(arquivo.loc[45])