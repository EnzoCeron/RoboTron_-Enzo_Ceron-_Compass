# Printe o nome do Ator que ganhou o Oscar em 1993.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

# separando o nome do ator em uma variavel e pritando ele
ano = arquivo['Name'][arquivo['Year'] == 1993]
print(ano.to_string(index=True))