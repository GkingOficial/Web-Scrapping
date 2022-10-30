import json

with open("json/vehicles_to_search.json") as jsonFile:
  vehicles_to_search = json.load(jsonFile)

with open("json/indices_de_busca.json") as jsonFile:
  indices = json.load(jsonFile)

# Variar indices
def update_index():
  right = True
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
        indices["modelo_especifico"] = -1
        indices["modelo_base"] = -1
        indices["marca"] == -1

        print("ACABOU os modelos para busca!")
        right = False
  
  print(indices)
  with open("json/indices_de_busca.json", "w") as jsonFile:
    json.dump(indices, jsonFile)
  
  indices["modelo_especifico"] += 1
  return right

def read_json(path):
  with open(path) as jsonFile:
    json_object = json.load(jsonFile)
  return json_object