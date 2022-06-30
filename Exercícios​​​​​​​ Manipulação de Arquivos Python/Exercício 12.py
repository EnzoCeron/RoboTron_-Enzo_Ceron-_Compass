# Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

# separando os nomes dos atores em variaveis e pritando
ano = arquivo['Name'][arquivo['Year'] == 1991]
ano2 = arquivo['Name'][arquivo['Year'] == 2016]
print(ano.to_string(index=True), ano2.to_string(index=True))
