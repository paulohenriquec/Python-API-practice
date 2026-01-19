#%%
#1ª etapa: importar as bibliotecas
import requests
import pandas as pd
import json
from tqdm import tqdm

data = []
fonte_externa = dict()

#%%
#2ª etapa: realizar requisição dinâmica
while True:
    #Pego a entrada do usuário
    cep = input("Digite qual CEP você deseja pesquisar: ")

    #Verifico se ele quer encerrar a busca
    if cep == "sair" or cep == "":
        break
    
    #Faço a requisição
    url = "https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url.format(cep=cep))

    #Se a requisição tiver sido bem sucedida, eu salvo o retorno json na minha lista data
    if resp.status_code == 200:
        data.append(resp.json())
#%%
#3ª etapa: salvar em um arquivo json
# estou abrindo um arquivo chamado ceps.json no modelo de escrita com a codificação utf-8 e estou salvando os dados de data, nesse arquivo
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(data, open_file, ensure_ascii=False, indent=4)
#%%
#4ª etapa: conversão em dataframe e csv
df = pd.DataFrame(data)
df.to_csv("ceps.csv", sep=";")

#%%
#5ª etapa: leitura de ceps de uma fonte externa
with open("Tabela de CEPs Brasileiros por Região.csv", "r") as open_file:
    lines = open_file.readlines()

keys = lines[0].strip("\n").split(",")

for k in keys:
    fonte_externa[k] = []

for l in lines[1:]:
    value = l.strip("\n").split(",")

    for i in range(len(value)):
        fonte_externa[keys[i]].append(value[i])

print(fonte_externa)

##PRÓXIMO PASSO, PEGAR OS CEPS DESSA LISTA E FAZER A REQUISIÇÃO