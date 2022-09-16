
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Faz o Web-Scrapping para algum site
values = []

def web_scrapping():
    '''
    url = "https://www.youtube.com/"
    '''
    url = "https://veiculos.fipe.org.br/"

    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)

    # Carregar a página
    driver.get(url)
    time.sleep(3)

    substring = '/html/body/div[1]/section[2]/div[1]/div[1]/ul/li[1]'

    # Clicar na tabela de Carros
    element = substring + '/a/div[2]'
    element = substring + ''
    element = substring + '/a'

    cars_selector_li = driver.find_element_by_class_name("ilustra")
    cars_selector_li.click()
    time.sleep(3)

    # Selecionar a parte da data dos dados
    driver.find_element_by_css_selector("#selectTabelaReferenciacarro_chosen > a:nth-child(1)").click()
    time.sleep(2)

    # Escolher determinada data
    element = substring + f"/div/article[1]/div[1]/div/ul/li[1]"
    driver.find_element_by_css_selector(f"li.active-result:nth-child(1)").click()
    time.sleep(1)

    # Clicar na parte de selecionar a marca do veiculo
    element = substring + '/div/article[1]/div[3]/div[1]/div/div/a'
    driver.find_element_by_css_selector('#selectMarcacarro_chosen > a:nth-child(1)').click()
    time.sleep(1)

    # Escolher determinada marca
    element = substring + '/div/article[1]/div[3]/div[1]/div/div/div/ul/li[1]'
    driver.find_element_by_css_selector('#selectMarcacarro_chosen > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1)').click()
    time.sleep(1)

    # Clicar na parte de selecionar o modelo do veiculo
    element = substring + '/div/article[1]/div[3]/div[2]/div[1]/div[1]/a'
    driver.find_element_by_css_selector('#selectAnoModelocarro_chosen > a:nth-child(1)').click()
    time.sleep(1)

    # Escolher determinado modelo
    element = substring + "/div/article[1]/div[3]/div[2]/div[1]/div[1]/div/ul/li[1]"
    driver.find_element_by_css_selector("li.active-result:nth-child(1)").click()
    time.sleep(1)

    # Clicar na parte de selecionar o ano do veiculo
    element = substring + '/div/article[1]/div[3]/div[2]/div[2]/div/a'
    driver.find_element_by_css_selector("#selectAnocarro_chosen").click()
    time.sleep(1)

    # Escolher ano do veiculo
    element = substring + "/div/article[1]/div[3]/div[2]/div[2]/div/div/ul/li[1]"
    driver.find_element_by_css_selector("li.active-result:nth-child(1)").click()
    time.sleep(1)

    # Pesquisar
    element = '//*[@id="buttonPesquisarcarro"]'
    driver.find_element_by_xpath(element).click()
    time.sleep(1)

    element = substring + '/div/article[1]/div[3]/div[4]/table/tbody/tr[8]/td[2]/p'
    value = driver.find_element_by_css_selector("#resultadoConsultacarroFiltros > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(2) > p:nth-child(1)").text
    print("Preço médio com ano-modelo[1]: " + value)
    time.sleep(1)

    values.append(value)

    driver.find_element_by_css_selector("#buttonLimparPesquisarcarro > a:nth-child(1)").click()
    time.sleep(1)

    driver.quit()

web_scrapping()
print(values)