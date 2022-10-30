import json

with open("json/vehicles_to_search.json") as jsonFile:
  vehicles_to_search = json.load(jsonFile)

with open("json/indices_de_busca.json") as jsonFile:
  indices = json.load(jsonFile)

# Variar indices
def update_index():
  try:
    print(
      vehicles_to_search
        [indices["marca"]]
        ["modelos_base"]
        [indices["modelo_base"]]
        [indices["modelo_especifico"]]
    )

  except IndexError:
    indices["modelo_especifico"] = 0
    indices["modelo_base"] += 1

    try:
      print(
        vehicles_to_search
          [indices["marca"]]
          ["modelos_base"]
          [indices["modelo_base"]]
          [indices["modelo_especifico"]]
      )
    except IndexError:
      indices["modelo_especifico"] = 0
      indices["modelo_base"] = 0
      indices["marca"] += 1

      try:
        print(
          vehicles_to_search
            [indices["marca"]]
            ["modelos_base"]
            [indices["modelo_base"]]
            [indices["modelo_especifico"]]
        )
      except IndexError:
        print("ACABOU os modelos para busca!")
        raise IndexError
  
  print(indices)
  with open("indices_de_busca.json", "w") as jsonFile:
    json.dump(indices, jsonFile)
  
  indices["modelo_especifico"] += 1
