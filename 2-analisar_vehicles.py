from Vehicle_Search import Vehicle_Search
import util

vehicles = util.read_json("json/vehicles_2015.json")
# util.print_formatted_json(vehicles)

mes_busca = "janeiro"
ano_busca = 2015
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

try:
  vehicles_to_search = util.read_json("json/teste_2015.json")
except:
  vehicles_to_search = []

for i, category in enumerate(vehicles["vehicles"]):
  list_vehicles = category[categories_names[i]]

  vs = Vehicle_Search()
  vs.setup()
  for vehicle in list_vehicles:
    vehicle_json = {}

    vs.marca = vehicle["marca"]
    vs.modelo_base = vehicle["modelo"]
    vs.mes_busca = mes_busca
    vs.ano_busca = ano_busca

    print("="*20)
    print(vs.modelo_base)
    print("="*20)
    vehicle_names = vs.execution()

    vehicle_json["marca"] = vehicle["marca"]
    vehicle_json["modelos_base"] = []
    vehicle_json["modelos_base"].append(vehicle_names)

    vehicles_to_search.append(vehicle_json)
    util.print_formatted_json(vehicle_json)

    util.update_json("json/teste_2015.json", vehicles_to_search)
  
  vs.close()