import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping

computer_id = 1
number_of_computers = 3

def get_vehicles_to_search():
  vehicles_to_search = util.read_json("json/vehicles_to_search.json")

  return vehicles_to_search

def get_indices_de_busca(vehicles_to_search):
  vehicles_to_search_length = len(vehicles_to_search)

  bd = MongoDBWeb(vehicles_to_search_length, number_of_computers)
  indices_de_busca = bd.get_indexes(computer_id)

  return indices_de_busca

def run_web_scrapping(indices_de_busca, vehicles_to_search):
  web = Web_Scrapping(
    indices_de_busca,
    vehicles_to_search,
    computer_id,
    number_of_computers
  )
  web.get_vehicles_with_price()

  # Salva no arquivo vehicles_with_price.json
  web.execution()

def save_BD():
  bd = MongoDBWeb()
  bd.persistent("json/vehicles_with_price.json")

