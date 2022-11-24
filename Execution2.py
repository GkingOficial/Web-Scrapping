import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping
from settings import number_of_computers, computer_id

def get_vehicles_to_search():
  vehicles_to_search = util.read_json("json/vehicles_to_search.json")
  # print(vehicles_to_search)

  return vehicles_to_search

def get_indices_de_busca(vehicles_to_search):
  vehicles_to_search_length = len(vehicles_to_search)
  # print(vehicles_to_search_length)

  bd = MongoDBWeb(vehicles_to_search_length, number_of_computers)
  indices_de_busca = bd.get_indexes(computer_id)
  # print(indices_de_busca)

  return indices_de_busca

def run_web_scrapping(indices_de_busca, vehicles_to_search):
  web = Web_Scrapping(
    indices_de_busca=indices_de_busca,
    vehicles_to_search=vehicles_to_search,
    computer_id=computer_id,
    number_of_computers=number_of_computers
  )
  web.get_vehicles_with_price()
  # print(web.boundaries_for_computers)

  web.execution()

def save_BD():
  bd = MongoDBWeb()
  vehicles_with_price = util.read_json("json/vehicles_with_price.json")
  dictionary_of_values = {
    "vehicles": vehicles_with_price
  }
  bd.persistent(dictionary_of_values)

vehicles_to_search = get_vehicles_to_search()
indices_de_busca = get_indices_de_busca(vehicles_to_search)

run_web_scrapping(indices_de_busca, vehicles_to_search)