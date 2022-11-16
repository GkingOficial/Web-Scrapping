import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping

def get_indices_de_busca():
  bd = MongoDBWeb()
  indices_de_busca = bd.get_indexes()

  return indices_de_busca

def get_vehicles_to_search():
  vehicles_to_search = util.read_json("json/vehicles_to_search.json")

  return vehicles_to_search

def run_web_scrapping():
  indices_de_busca = get_indices_de_busca()
  vehicles_to_search = get_vehicles_to_search()

  web = Web_Scrapping(indices_de_busca, vehicles_to_search)
  web.get_vehicles_with_price()

  # Salvar no arquivo vehicles_with_price.json
  web.execution()

def save_BD():
  bd = MongoDBWeb()
  bd.persistent("json/vehicles_with_price.json")

run_web_scrapping()
save_BD()
