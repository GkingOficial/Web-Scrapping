import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Armazena os valores resultantes do web scrapping
values = []

# Site onde sera realizado o web scrapping
url = "https://veiculos.fipe.org.br/"

# Seletor das opcoes de busca
cars_selector = '#front > div.content > div.tab.vertical.tab-veiculos > ul > li:nth-child(1) > a'

# Seletor da data referencia
time_period_selector = '#selectTabelaReferenciacarro_chosen > a'

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

def web_scrapping2():

  # Seleciona o seletor das marcas
  driver.find_element(By.CSS_SELECTOR, brand_selector).click()
  time.sleep(1)
  
  # Filtro da marca desejada
  driver.find_element(By.CSS_SELECTOR, input_brand_selector).send_keys("Volvo")
  time.sleep(1)

  # Seleciona a primeira marca disponivel (marca desejada)
  driver.find_element(By.CSS_SELECTOR, item_brand_selector).click()
  time.sleep(1)

  # Seleciona o seletor dos modelos
  driver.find_element(By.CSS_SELECTOR, model_selector).click()
  time.sleep(1)
  # Filtro do modelo desejado
  driver.find_element(By.CSS_SELECTOR, input_model_selector).send_keys("850")
  time.sleep(1)

  # Pega todos os filhos da <ul> de modelos
  ul_model_element = driver.find_element(By.CSS_SELECTOR, ul_model_selector)
  ul_model_element_children = ul_model_element.find_elements(By.XPATH, "./*")

  # Iteracao para cada modelo
  for i in range(len(ul_model_element_children)):
    print(f"i = {i}")

    if i != 0:
      # Seleciona o seletor dos modelos
      driver.find_element(By.CSS_SELECTOR, model_selector).click()
      time.sleep(1)

      # Filtro do modelo desejado
      driver.find_element(By.CSS_SELECTOR, input_model_selector).send_keys("850")
      time.sleep(1)
    
    item_model_selector = f'li.active-result:nth-child({i + 1})'

    # Seleciona modelo desejado
    driver.find_element(By.CSS_SELECTOR, item_model_selector).click()
    time.sleep(1)

    # Selecionar seletor dos anos-modelo
    driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > a').click()
    time.sleep(1)

    # Pega todos os filhos da <ul> de anos-modelo
    ul_year_model_element = driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > div > ul')
    ul_year_model_element_children = ul_year_model_element.find_elements(By.XPATH, "./*")
    
    for j in range(len(ul_year_model_element_children)):
      print(f"j = {j}")

      if j != 0:
        # Seleciona seletor dos anos-modelo
        driver.find_element(By.CSS_SELECTOR, '#selectAnocarro_chosen > a:nth-child(1)').click()
        time.sleep(1)

      item_year_model_selector = f'li.active-result:nth-child({j + 1})'

      # Seleciona o ano-modelo desejado
      driver.find_element(By.CSS_SELECTOR, item_year_model_selector).click()
      time.sleep(1)

      # Seleciona "Pesquisar"
      driver.find_element(By.CSS_SELECTOR, search_button_selector).click()
      time.sleep(1)

      # Pegar o preço do veiculo

      # Limpar pesquisa
      driver.find_element(By.CSS_SELECTOR, clear_search_selector).click()
      time.sleep(1)

  driver.quit()

web_scrapping1()
web_scrapping2()