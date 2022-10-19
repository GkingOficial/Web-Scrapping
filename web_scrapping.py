import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Armazena os valores resultantes do web scrapping
values = []

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

option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)

def web_scrapping1():
  # Carregar a página
  driver.get(url)
  time.sleep(3)

  # Selecionar opcao de busca de carros
  driver.find_element(By.CSS_SELECTOR, cars_selector).click()
  time.sleep(1)

  # Seleciona o periodo
  driver.find_element(By.CSS_SELECTOR, time_period_selector).click()
  time.sleep(1)

def web_scrapping2(marca, modelo):

  # Seleciona o input do periodo
  driver.find_element(By.CSS_SELECTOR, input_time_period_selector).send_keys("janeiro/2020")
  time.sleep(1)

  driver.find_element(By.CSS_SELECTOR, item_time_period_selector).click()

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

  for ano in range(2010, 2012 + 1):
    print(f"Ano: {ano}")

    if ano == 2010:
      # Selecionar seletor dos anos-modelo
      driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > a').click()
      time.sleep(1)

    # Selecionar o input dos ano-modelo
    input = driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > div > div > input[type=text]')
    time.sleep(1)

    for i in range(0, 4):
      input.send_keys(Keys.BACK_SPACE)

    if ano == 2022:
      input.send_keys("zero")
    else:
      input.send_keys(str(ano))

    time.sleep(1)

    # Pega todos os filhos da <ul> de anos-modelo
    ul_year_model_element = driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > div > ul')
    ul_year_model_element_children = ul_year_model_element.find_elements(By.XPATH, "./*")

    time.sleep(1)
  
    if(ul_year_model_element_children[0].get_attribute("class") == 'no-results'):
      print(f"Quantidade de anos-modelo: 0")
    else:
      print(f"Quantidade de anos-modelo: {len(ul_year_model_element_children)}")

      item_year_model_selector = f'li.active-result:nth-child({0 + 1})'

      # Seleciona o ano-modelo desejado
      driver.find_element(By.CSS_SELECTOR, item_year_model_selector).click()
      time.sleep(1)

      # Seleciona "Pesquisar"
      driver.find_element(By.CSS_SELECTOR, search_button_selector).click()
      time.sleep(1)

      # Pegar o preço do veiculo
      price = driver.find_element(By.CSS_SELECTOR, '#resultadoConsultacarroFiltros > table > tbody > tr.last > td:nth-child(2) > p').text
      print(f"Preço: {price}")

      # # Limpar pesquisa
      # driver.find_element(By.CSS_SELECTOR, clear_search_selector).click()
      # time.sleep(1)

  driver.quit()

web_scrapping1()
web_scrapping2("VolksWagen", "Fox")