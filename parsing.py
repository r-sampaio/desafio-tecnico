import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver")
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get("https://www.acordacidade.com.br")

# html_souce = browser.page_source
# print(html_souce)

time.sleep(5)

lupa = browser.find_element_by_xpath("//div[@class='busca']").click()
# busca = browser.find_element_by_name("busca")
# busca = browser.find_element_by_xpath("//div[@class='busca']//input[@type='text']")
busca = browser.find_element_by_xpath("//*[@placeholder='Pesquisar']")
# busca = browser.findElement(By.id("inputbusca")).sendKeys("falta de agua")
# busca.clear()
busca.send_keys("falta de agua")
busca.send_keys(Keys.RETURN)

time.sleep(10)

noticia = browser.find_element_by_xpath("//div[@class='box-noticia2 box-noticia4 first']//h2[@class='tt_capa']")
url = noticia.find_element_by_tag_name('a').get_attribute('href')

# href = browser.find_element_by_id("noticias")
# print(noticias.text)

browser.get(url)

os.system('cls')

print(url)

titulo = browser.find_element_by_class_name("titulo")
print(titulo.text)
print()

materia = browser.find_elements_by_xpath("//div[@id='tamanhotexto']//p")
for c in materia:
    print(c.text)

browser.quit()
