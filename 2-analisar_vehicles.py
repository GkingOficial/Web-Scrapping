from Vehicle_Search import Vehicle_Search
import util

vehicles = util.read_json("json/vehicles.json")
util.print_formatted_json(vehicles)

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

for i, category in enumerate(vehicles["vehicles"]):
  list_vehicles = category[categories_names[i]]

  for vehicle in list_vehicles:
    vs = Vehicle_Search(vehicle["marca"], vehicle["modelo"], mes_busca, ano_busca)
    vehicle_names = vs.execution()

    util.print_formatted_json(vehicle_names)