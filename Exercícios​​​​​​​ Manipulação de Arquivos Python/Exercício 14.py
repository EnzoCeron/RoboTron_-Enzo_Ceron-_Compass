# Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

# importando a biblioteca do pandas
import pandas as pd

# lendo e salvando o arquivo em uma variavel
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

# criando uma nova coluna com nomes e idades dos atores
arquivo["Name_age"] = arquivo["Name"] + ' ' + arquivo["Age"].apply(str)

# definindo os indexes de qual linha quero printar e a coluna especifica
print(arquivo.loc[59:71]["Name_age"])
