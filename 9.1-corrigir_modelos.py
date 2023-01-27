import util
from MongoDBWeb import MongoDBWeb
from web_scrapping import Web_Scrapping

from settings import number_of_computers, computer_id, mini_batch
from settings import vehicles_with_price_path, incomplete_to_search_path
from settings import incomplete_path, modelo_atual_path

def get_vehicles_to_search():
  vehicles_to_search = util.read_json(incomplete_to_search_path)

  return vehicles_to_search

def get_indices_de_busca(vehicles_to_search):
  vehicles_to_search_length = len(vehicles_to_search)

  bd = MongoDBWeb(vehicles_to_search_length, number_of_computers)
  indices_de_busca = bd.get_indexes(computer_id)

  return indices_de_busca

def run_web_scrapping(indices_de_busca, vehicles_to_search):
  # Pegar o elemento de incomplete.json e passar para modelo atual
  incomplete = util.read_json(incomplete_path)
  util.update_json(modelo_atual_path, incomplete[0])

  web = Web_Scrapping(
    indices_de_busca=indices_de_busca,
    vehicles_to_search=vehicles_to_search,
    computer_id=computer_id,
    number_of_computers=number_of_computers
  )
  web.get_vehicles_with_price()
  web.execution(mini_batch)
  
  # Remover primeiro elemento de incomplete.json
  del incomplete[0]
  util.update_json(incomplete_path, incomplete)


def save_BD():
  bd = MongoDBWeb()
  vehicles_with_price = util.read_json(vehicles_with_price_path)
  
  bd.persistent(vehicles_with_price)

def clean_vehicles_with_price():
  util.clear_json(vehicles_with_price_path)
  

vehicles_to_search = get_vehicles_to_search()
indices_de_busca = get_indices_de_busca(vehicles_to_search)

run_web_scrapping(indices_de_busca, vehicles_to_search)

save_BD()
clean_vehicles_with_price()