#%%
#1ª etapa: importar as bibliotecas
import requests
import pandas as pd
import json
from tqdm import tqdm

#%%
#2ª etapa: realizar requisição dinâmica
cep = input("Digite qual CEP você deseja pesquisar: ")

url = "https://viacep.com.br/ws/{cep}/json/"

resp = requests.get(url.format(cep=cep))

print(resp)
