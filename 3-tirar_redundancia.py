import util

anos = [ 2015, 2022 ]

vehicles_to_search = util.read_json(f"json/vehicles_to_search_{anos[0]}.json")
vehicles_to_search_2022 = util.read_json(f"json/vehicles_to_search_{anos[1]}.json")

for vehicle_2022 in vehicles_to_search_2022:
  occurances = vehicles_to_search.count(vehicle_2022)
  if occurances == 0:
    vehicles_to_search.append(vehicle_2022)

util.update_json("json/vehicles_to_search.json", vehicles_to_search)