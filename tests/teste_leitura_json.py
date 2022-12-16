import json
from settings import verbose

with open("vehicles_to_search.json") as jsonFile:
  dados = json.load(jsonFile)

dados_formatted = json.dumps(dados, indent=2)

if verbose:
  print(dados)
  print(dados_formatted)