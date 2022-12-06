from Vehicle_Search import Vehicle_Search
import util
import json

vehicles = util.read_json("json/vehicles.json")
util.print_formatted_json(vehicles)

def update_json(jsonPath, jsonObject):
  with open(jsonPath, "w") as jsonFile:
    json.dump(jsonObject, jsonFile, indent=2)

mes_busca = "setembro"
ano_busca = 2019
categories_names = [
  "Hatch compacto",
  "Sedã compacto",
  "Aventureiro compacto",
  "SUV compacto",
  "Familiar compacto",
  "Picape compacta",
  "SUV médio",
  "Sedã médio",
  "Picape compacta-média",
  "Picape média"
]

vehicles_to_search = []

for i, category in enumerate(vehicles["vehicles"]):
  list_vehicles = category[categories_names[i]]

  for vehicle in list_vehicles:
    vehicle_json = {}

    vs = Vehicle_Search(vehicle["marca"], vehicle["modelo"], mes_busca, ano_busca)
    vehicle_names = vs.execution()

    vehicle_json["marca"] = vehicle["marca"]
    vehicle_json["modelos_base"] = []
    vehicle_json["modelos_base"].append(vehicle_names)

    vehicles_to_search.append(vehicle_json)

    util.print_formatted_json(vehicles_to_search)