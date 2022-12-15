from Vehicle_Search import Vehicle_Search
import util

ano_considerado = 2022
mes_busca = "janeiro"
ano_busca = 2015

vehicles = util.read_json(f"json/vehicles_{ano_considerado}.json")

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
  vehicles_to_search = util.read_json(f"json/vehicles_to_search_{ano_considerado}.json")
except:
  vehicles_to_search = []

vehicles_discarded_count = 0
vehicles_count = 0
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

    if len(vehicle_names) > 0:
      vehicle_json["marca"] = vehicle["marca"]
      vehicle_json["modelos_base"] = []
      vehicle_json["modelos_base"].append(vehicle_names)

      vehicles_to_search.append(vehicle_json)
      util.print_formatted_json(vehicle_json)

      util.update_json(f"json/vehicles_to_search_{ano_considerado}.json", vehicles_to_search)

      vehicles_count += len(vehicle_names)
    else:
      print("Veiculo descartado:")
      print(f'{vehicle["marca"]}/{vehicle["modelo"]}')
      vehicles_discarded_count += 1
  
  print("Modelos considerados:", vehicles_count)
  print("Modelos_base descartados:", vehicles_discarded_count)
  vs.close()