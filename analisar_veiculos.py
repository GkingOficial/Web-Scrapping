import time
import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Site onde sera realizado o web scrapping
url = "https://veiculos.fipe.org.br/"


# Seletor das opcoes de busca
cars_selector = '#front > div.content > div.tab.vertical.tab-veiculos > ul > li:nth-child(1) > a'

# Seletor do seletor de data referencia
time_period_selector = '#selectTabelaReferenciacarro_chosen > a'

# Input da data referencia
input_time_period_selector = '#selectTabelaReferenciacarro_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'

# Item da data referencia
item_time_period_selector = '.active-result'

# Seletor da marca do veiculo
brand_selector = '#selectMarcacarro_chosen > a'

# Seletor da entrada da marca do veiculo desejado
input_brand_selector = '#selectMarcacarro_chosen > div > div > input[type=text]'

# Seletor da lista de marcas
item_brand_selector = '#selectMarcacarro_chosen > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1)'

# Seletor do modelo do veiculo
model_selector = '#selectAnoModelocarro_chosen > a:nth-child(1)'

# Seletor da entrada do modelo do veiculo desejado
input_model_selector='#selectAnoModelocarro_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'

# Seletor da lista de modelos
ul_model_selector = '#selectAnoModelocarro_chosen > div:nth-child(2) > ul:nth-child(2)'

# Seletor do botao 'Pesquisar'
search_button_selector = '#buttonPesquisarcarro'

# Seletor do 'Limpar Pesquisa'
clear_search_selector = '#buttonLimparPesquisarcarro > a'

# Seletor do preço
price_vehicle = '#resultadoConsultacarroFiltros > table > tbody > tr.last > td:nth-child(2) > p'

# Seletor dos anos-modelo
year_model_selector ='#selectAnocarro_chosen > a'

# Seletor do input dos anos-modelo
input_year_model_selector = '#selectAnocarro_chosen > div > div > input[type=text]'

# Seletor do input do ano-modelo
ul_year_model_selector = '#selectAnocarro_chosen > div > ul'

# Seletor do preço
price_vehicle = '#resultadoConsultacarroFiltros > table > tbody > tr.last > td:nth-child(2) > p'

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

wait = WebDriverWait(driver, 10)

# Configura inicialmente o web_scrapping
def setup():
  # Carregar a página
  driver.get(url)
  time.sleep(3)

  # Selecionar opcao de busca de carros
  driver.find_element(By.CSS_SELECTOR, cars_selector).click()
  time.sleep(1)

  # Seleciona o periodo
  driver.find_element(By.CSS_SELECTOR, time_period_selector).click()
  time.sleep(1)

# Lista os todos os modelos que possuem aquele modelo_base
def get_models_from_model_base(marca, modelo_base, mes_busca, ano_busca):
  # Seleciona o input do periodo
  driver.find_element(By.CSS_SELECTOR, input_time_period_selector).send_keys(f"{mes_busca}/{ano_busca}")
  time.sleep(3)

  period_selector = '#selectTabelaReferenciacarro_chosen > div > ul > li'

  # Seleciona o primeiro item do período
  elemento = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, period_selector))
  )
  elemento.click()

  # Seleciona o seletor das marcas
  driver.find_element(By.CSS_SELECTOR, brand_selector).click()
  time.sleep(1)
  
  # Filtro da marca desejada
  driver.find_element(By.CSS_SELECTOR, input_brand_selector).send_keys(marca)
  time.sleep(1)

  # Seleciona a primeira marca disponivel (marca desejada)
  driver.find_element(By.CSS_SELECTOR, item_brand_selector).click()
  time.sleep(1)

  # Seleciona o seletor dos modelos
  driver.find_element(By.CSS_SELECTOR, model_selector).click()
  time.sleep(1)

  # Filtro do modelo desejado
  driver.find_element(By.CSS_SELECTOR, input_model_selector).send_keys(modelo_base)
  time.sleep(1)

  # Pega todos os filhos da <ul> de modelos
  ul_model_element = driver.find_element(By.CSS_SELECTOR, ul_model_selector)
  ul_model_element_children = ul_model_element.find_elements(By.XPATH, "./*")

  models_names = []
  for index, item in enumerate(ul_model_element_children):
    models_names.append((index, item.text))
  
  return models_names

# Retorna lista com as palavras que temos
def return_models_with_an_especific_word(list_models, word):
  new_models = []
  for model in list_models:
    if model[1].count(word):
      new_models.append(model)
  
  return new_models

def is_float_number(value):
  if value.isdigit():
    return False
  return value.replace('.','',1).isdigit()

# Retorna o número contido na string
def return_float_number(string):
  list_strings = string.split(" ")

  for item in list_strings:
    if is_float_number(item):
      value = float(item)
      return value
  return None




# Busca do inicio do periodo
setup()
models_names = get_models_from_model_base("Hyundai", " HB20", "setembro", 2019)

for word in "Aut.", "Mec.":
  new_models_names = return_models_with_an_especific_word(models_names, word)
  print(json.dumps(new_models_names, indent=2))

  list_values = []
  for index, model in enumerate(new_models_names):
    float_number = return_float_number(model[1])
    if float_number != None:
      list_values.append((index, float_number))
  print(json.dumps(list_values, indent=2))

driver.close()
