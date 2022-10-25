import json

with open("vehicles_to_search.json") as jsonFile:
  dados = json.load(jsonFile)

# dados = {
#   "nome": 'Daniel Alencar Penha Carvalho',
#   "Idade": 21 
# }

dados_formatted = json.dumps(dados, indent=2)

print(dados)
print(dados_formatted)