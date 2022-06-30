# A) Crie uma “aplicação” em loop que tenha uma opção para listar todos os elementos da tabela,
# porém mostrando apenas uma propriedade do elemento. Ex: listar todos os nomes dos elementos na tabela.

# B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

# C) Listar todos os dados de todos os elementos inseridos.

# importando a biblioteca do pandas
import pandas as pd


# definindo as funcoes para o obejtivo A
def simbolos():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['Simbolo'])
    simbolo = arquivo.to_string(index=True)
    return simbolo


def nomes():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['Nome'])
    nome = arquivo.to_string(index=True)
    return nome


def numeroatomico():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['NumeroAtomico'])
    NumeroAtomico = arquivo.to_string(index=True)
    return NumeroAtomico


def linha():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['Linha'])
    linhas = arquivo.to_string(index=True)
    return linhas


def coluna():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['Coluna'])
    colunas = arquivo.to_string(index=True)
    return colunas


def estadosisico():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',', usecols=['EstadoFisico'])
    estado = arquivo.to_string(index=True)
    return estado


# funcao do objetivo B
def listardados(simbolo):
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',')
    if simbolo == "Kr":
        return print(arquivo.loc[0])
    elif simbolo == "S":
        return print(arquivo.loc[1])
    elif simbolo == "Ar":
        return print(arquivo.loc[2])
    elif simbolo == "Ca":
        return print(arquivo.loc[3])
    elif simbolo == "Sm":
        return print(arquivo.loc[4])
    elif simbolo == "Sc":
        return print(arquivo.loc[5])
    elif simbolo == "I":
        return print(arquivo.loc[6])
    elif simbolo == "Eu":
        return print(arquivo.loc[7])
    elif simbolo == "N":
        return print(arquivo.loc[8])
    elif simbolo == "Hg":
        return print(arquivo.loc[9])
    elif simbolo == "Fr":
        return print(arquivo.loc[10])
    elif simbolo == "Pb":
        return print(arquivo.loc[11])
    elif simbolo == "Po":
        return print(arquivo.loc[12])
    elif simbolo == "B":
        return print(arquivo.loc[13])
    elif simbolo == "Re":
        return print(arquivo.loc[14])
    else:
        print("ERROR")


# funcao do objetivo C
def retornatudo():
    arquivo = pd.read_csv('Elementos.csv', encoding='UTF-8', sep=',')
    tudo = arquivo.to_string(index=True)
    return tudo


# loop do jogo
while True:
    print("Ações Possiveis: \n"
          "1 - Seleciona um tipo de dados especifico para retornar \n"
          "2 - Retorna todos os dados de um elemento com base no simbolo inserido \n"
          "3 - Retorna todos os dados de todos os elementos")
    print("Se deseja sair do programa digite 4")
    modo = int(input("Insira o modo desejado de consulta: "))
    if modo == 1:
        print("As colunas disponiveis são: \n"
              "Simbolo \n"
              "Nome \n"
              "NumeroAtomico \n"
              "Linha \n"
              "Coluna \n"
              "EstadoFisico")
        colunainput = input("Insira o nome da coluna que deseja consultar: ")
        if colunainput == "Simbolo":
            print(simbolos())
        elif colunainput == "Nome":
            print(nomes())
        elif colunainput == "NumeroAtomico":
            print(numeroatomico())
        elif colunainput == "Linha":
            print(linha())
        elif colunainput == "Coluna":
            print(coluna())
        elif colunainput == "EstadoFisico":
            print(estadosisico())
    elif modo == 2:
        print("Os elementos presentes na tabela são: Kr, S, Ar, Ca, Sm, Sc, I, Eu, N, Hg, Fr, Pb, Po, B, Re")
        simbolou = input("Insira o simbolo desejado: ")
        print(listardados(simbolou))
    elif modo == 3:
        print("aqui estão todos os dados: ")
        print(retornatudo())
    elif modo == 4:
        break
