import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

values = []
# Faz o Web-Scrapping para algum site
def web_scrapping():

    url = "https://veiculos.fipe.org.br/"

    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)

    # Carregar a página
    driver.get(url)
    time.sleep(3)

    # driver.find_element
    # driver.find_elements

    # Clicar na tabela de carros
    cars_selector_li = driver.find_element(By.CLASS_NAME, "ilustra")
    cars_selector_li.click()
    time.sleep(3)

    # Selecionar a parte da data dos dados
    driver.find_element(By.CSS_SELECTOR, "#selectTabelaReferenciacarro_chosen > a:nth-child(1)").click()
    time.sleep(3)

    # Escolher determinada data
    driver.find_element(By.CSS_SELECTOR, f"li.active-result:nth-child(1)").click()
    time.sleep(3)

    for index_model in range(1, 2):

        # Clicar na parte de selecionar a marca do veiculo
        driver.find_element(By.CSS_SELECTOR, '#selectMarcacarro_chosen > a:nth-child(1)').click()
        time.sleep(3)

        # Escolher determinada marca
        driver.find_element(By.CSS_SELECTOR, '#selectMarcacarro_chosen > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1)').click()
        time.sleep(3)

        # Clicar na parte de selecionar o modelo do veiculo
        driver.find_element(By.CSS_SELECTOR, '#selectAnoModelocarro_chosen > a:nth-child(1)').click()
        time.sleep(3)

        # Escolher determinado modelo
        driver.find_element(By.CSS_SELECTOR, f"li.active-result:nth-child({index_model})").click()
        time.sleep(3)

        for index_year_model in range(1, 2):

            # Clicar na parte de selecionar o ano do veiculo
            driver.find_element(By.CSS_SELECTOR, "#selectAnocarro_chosen").click()
            time.sleep(3)

            # Escolher ano do veiculo
            driver.find_element(By.CSS_SELECTOR, f"li.active-result:nth-child({index_year_model})").click()
            time.sleep(3)

            # Pesquisar
            element = '//*[@id="buttonPesquisarcarro"]'
            driver.find_element(By.XPATH, element).click()
            time.sleep(3)
    
            value = driver.find_element(By.CSS_SELECTOR, "#resultadoConsultacarroFiltros > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > p:nth-child(1)").text
            print(f"Preço médio com ano-modelo[{index_year_model}]: " + value)
            time.sleep(3)

            values.append(value)

        driver.find_element(By.CSS_SELECTOR, "#buttonLimparPesquisarcarro > a:nth-child(1)").click()
        time.sleep(3)

    driver.quit()

web_scrapping()
print(values)