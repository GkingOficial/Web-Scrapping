import time
import json
import selectors_html

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException

# Site onde sera realizado o web scrapping
url = "https://veiculos.fipe.org.br/"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

wait = WebDriverWait(driver, 10)

# Configurar inicialmente o web_scrapping
def setup():
  # Carregar a página
  driver.get(url)
  time.sleep(3)

  # Selecionar opcao de busca de carros
  driver.find_element(By.CSS_SELECTOR, selectors_html.cars_selector).click()
  time.sleep(1)

  # Seleciona o periodo
  driver.find_element(By.CSS_SELECTOR, selectors_html.time_period_selector).click()
  time.sleep(1)

# Listar todos os modelos que possuem aquele modelo_base [(0, nome_0)]
def get_models_from_model_base(marca, modelo_base, mes_busca, ano_busca): 
  # Seleciona o input do periodo
  driver.find_element(By.CSS_SELECTOR, selectors_html.input_time_period_selector).send_keys(f"{mes_busca}/{ano_busca}")
  time.sleep(3)

  # Seleciona o primeiro item do período
  elemento = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, selectors_html.item_time_period_selector))
  )
  elemento.click()

  # Seleciona o seletor das marcas
  driver.find_element(By.CSS_SELECTOR, selectors_html.brand_selector).click()
  time.sleep(1)
  
  # Filtro da marca desejada
  driver.find_element(By.CSS_SELECTOR, selectors_html.input_brand_selector).send_keys(marca)
  time.sleep(1)

  # Seleciona a primeira marca disponivel (marca desejada)
  driver.find_element(By.CSS_SELECTOR, selectors_html.item_brand_selector).click()
  time.sleep(1)

  # Seleciona o seletor dos modelos
  driver.find_element(By.CSS_SELECTOR, selectors_html.model_selector).click()
  time.sleep(1)

  # Filtro do modelo desejado
  driver.find_element(By.CSS_SELECTOR, selectors_html.input_model_selector).send_keys(modelo_base)
  time.sleep(1)

  # Pega todos os filhos da <ul> de modelos
  ul_model_element = driver.find_element(By.CSS_SELECTOR, selectors_html.ul_model_selector)
  ul_model_element_children = ul_model_element.find_elements(By.XPATH, "./*")

  models_names = []
  for index, item in enumerate(ul_model_element_children):
    models_names.append((index, item.text))
  
  return models_names

# Web Scrapping
def search_models(marca, modelo_base, mes_busca, ano_busca):
  setup()
  return get_models_from_model_base(marca, modelo_base, mes_busca, ano_busca)






# Retornar lista dos modelos que possuem alguma palavra específica
def return_models_with_an_especific_word(list_models, word):
  new_models = []
  for model in list_models:
    if model[1].count(word):
      new_models.append(model)
  
  return new_models

# Retornar (True ou False) se for um número flutuante
def is_float_number(value):
  if value.isdigit():
    return False
  return value.replace('.','',1).isdigit()

# Retornar o número flutuante contido na string
def return_float_number(string):
  list_strings = string.split(" ")

  for item in list_strings:
    if is_float_number(item):
      value = float(item)
      return value
  return None





marca = "Hyundai"
modelo_base = "HB20"
mes_busca = "setembro"
ano_busca = 2019
words = ["Aut.", "Mec."]

vehicle_to_search = {
  "marca": "Hyundai",
  "modelos_base": []
}
models_names = search_models(marca, modelo_base, mes_busca, ano_busca)






# Retornar lista com maior e menor motorização de: marca e modelo_base
def get_larger_and_smaller_vehicle(marca, modelo_base, mes_busca, ano_busca, word):

  values_with_indexes = []
  new_models_names = return_models_with_an_especific_word(models_names, word)
  print(json.dumps(new_models_names, indent=2))

  list_values = []
  for model in new_models_names:
    float_number = return_float_number(model[1])
    if float_number != None:
      list_values.append((model[0], float_number))
  print(json.dumps(list_values, indent=2))

  maximum_value = max(list_values, key=lambda x:x[1])
  minimum_value = min(list_values, key=lambda x:x[1])

  values_with_indexes.append(maximum_value)
  values_with_indexes.append(minimum_value)
  return values_with_indexes

# Retornar lista de nomes dos modelos a partir da lista de indices
def get_names_from_indexes(list_indexes, list_names):
  new_list_names = []
  indexes_not_repeated = []

  for item in list_indexes:
    if item[0] is not indexes_not_repeated:
      new_list_names.append(list_names[item[0]][1])
      indexes_not_repeated.append(item[0])

  return new_list_names




values_with_indexes = get_larger_and_smaller_vehicle(marca, modelo_base, mes_busca, ano_busca, words[1])
new_list_names = get_names_from_indexes(values_with_indexes, models_names)

vehicle_to_search['modelos_base'].append(new_list_names)
print(json.dumps(vehicle_to_search, indent=2))

driver.close()
