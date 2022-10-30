import time
import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import util

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




anos = [
  2020
]

meses = [
  "janeiro"
]

anos_modelo = [
  2020, 2021, "zero"
]


# Identificador básico: [marca][modelo_base][modelo_especifico]
# Leitura do JSON dos veiculos que queremos buscar
with open("json/vehicles_to_search.json") as jsonFile:
  vehicles_to_search = json.load(jsonFile)
  vehicles_to_search_formatted = json.dumps(vehicles_to_search, indent=2)

# Busca dos indices de: marca, modelo_base e modelo_especifico
with open("json/indices_de_busca.json") as jsonFile:
  indices = json.load(jsonFile)


option = Options()
option.headless = False
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

# Retorna um dicionário com os valores correspondentes
def get_model_prices(anos, meses, marca, modelo, anos_modelo):

  vehicle_information = {
    "marca": marca,
    "modelo": modelo,
    "anos": {}
  }

  for ano_busca in anos:
    vehicle_information['anos'][ano_busca] = {}

    for mes_busca in meses:
      vehicle_information['anos'][ano_busca][mes_busca] = {}

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
      driver.find_element(By.CSS_SELECTOR, input_model_selector).send_keys(modelo)
      time.sleep(1)

      # Pega todos os filhos da <ul> de modelos
      ul_model_element = driver.find_element(By.CSS_SELECTOR, ul_model_selector)
      ul_model_element_children = ul_model_element.find_elements(By.XPATH, "./*")
      
      item_model_selector = f'li.active-result:nth-child({0 + 1})'

      # Seleciona modelo desejado
      driver.find_element(By.CSS_SELECTOR, item_model_selector).click()
      time.sleep(1)

      for ano_modelo_busca in anos_modelo:

        vehicle_information['anos'][ano_busca][mes_busca][ano_modelo_busca] = None

        print(f"Ano_modelo: {ano_modelo_busca}")

        if ano_modelo_busca == anos_modelo[0]:
          # Selecionar seletor dos anos-modelo
          driver.find_element(By.CSS_SELECTOR, year_model_selector).click()
          time.sleep(1)

        # Selecionar o input dos ano-modelo
        input = driver.find_element(By.CSS_SELECTOR, input_year_model_selector)
        time.sleep(1)

        for i in range(0, 4):
          input.send_keys(Keys.BACK_SPACE)

        input.send_keys(str(ano_modelo_busca))
        time.sleep(3)

        # Pega todos os filhos da <ul> de anos-modelo
        ul_year_model_element = driver.find_element(By.CSS_SELECTOR, ul_year_model_selector)
        ul_year_model_element_children = ul_year_model_element.find_elements(By.XPATH, "./*")

        time.sleep(3)
      
        if(ul_year_model_element_children[0].get_attribute("class") == 'no-results'):
          print(f"Quantidade de anos-modelo: 0")
        else:
          print(f"Quantidade de anos-modelo: {len(ul_year_model_element_children)}")

          item_year_model_selector = f'li.active-result:nth-child({0 + 1})'

          # Selecionar o ano-modelo desejado
          driver.find_element(By.CSS_SELECTOR, item_year_model_selector).click()
          time.sleep(1)

          # Selecionar "Pesquisar"
          driver.find_element(By.CSS_SELECTOR, search_button_selector).click()
          time.sleep(1)

          # Pegar o preço do veiculo
          price = driver.find_element(By.CSS_SELECTOR, price_vehicle).text
          vehicle_information['anos'][ano_busca][mes_busca][ano_modelo_busca] = price

          print(f"Preço: {price}\n")

      # Limpar pesquisa
      try:
        element = driver.find_element(By.CSS_SELECTOR, clear_search_selector)
        element.click()
        print("Limpando a pesquisa!\n")
        time.sleep(1)
      except ElementNotInteractableException:
        print("Não foi possível limpar a pesquisa!\n")

  return vehicle_information

with open("json/vehicles_with_price.json") as jsonFile:
  vehicles_with_price = json.load(jsonFile)

# Executions
setup()

while True:
  try:
    util.update_index()
  except IndexError:
    print("Não há mais indices disponiveis para consulta!")
    break

  vehicle_information = get_model_prices(
    anos, 
    meses, 
    vehicles_to_search
      [indices["marca"]]["marca"],
    vehicles_to_search
      [indices["marca"]]["modelos_base"]
      [indices["modelo_base"]]
      [indices["modelo_especifico"]],
    anos_modelo
  )

  vehicle_information_formatted = json.dumps(vehicle_information, indent=2)
  print(vehicle_information_formatted)

  vehicles_with_price.append(vehicle_information)
  with open("json/vehicles_with_price.json", "w") as jsonFile:
    json.dump(vehicles_with_price, jsonFile, indent=2)

  print("\n=======================\n")



# Fechamento de execução do web_scrapping
driver.quit()