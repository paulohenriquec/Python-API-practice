#%%
#1ª etapa: importar as bibliotecas
import requests
import pandas as pd
import json
from tqdm import tqdm

data = []

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
with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(data, open_file, ensure_ascii=False, indent=4)