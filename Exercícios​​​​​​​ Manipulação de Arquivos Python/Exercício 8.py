# Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal

# importando a biblioteca do pandas
import pandas as pd

# salvando o arquivo csv em uma variavel
arquivo = pd.read_csv('CSV.csv', encoding='UTF-8', sep=',')

# printando
print(arquivo)