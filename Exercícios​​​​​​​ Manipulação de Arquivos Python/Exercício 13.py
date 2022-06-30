# Crie mais uma coluna em tempo de execução juntando os dados movie e year

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

# criando a coluna e printando a mesma
arquivo["Movie_year"] = arquivo["Movie"] + ' ' + arquivo["Year"].apply(str)
print(arquivo["Movie_year"])