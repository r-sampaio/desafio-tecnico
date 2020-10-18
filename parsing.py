#!/usr/bin/python3

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys


chrome_options = Options()

# Executa o browser em background mostrando as informações no terminal
chrome_options.add_argument("--headless") # Para desativar, comente essa linha

# Desativa as mensagem de erro e infomações no terminal
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Cria a instancia com os paramentos passados para o browser e o caminho do driver Google
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")

# Abre o browser no site passado por paramentro
browser.get("https://www.acordacidade.com.br")

# Aguarda 5 segundos para que site carregue
time.sleep(5)

# Clica na lupa para que o campo de busca apareça
lupa = browser.find_element_by_xpath("//div[@class='busca']").click()

# Seleciona o campo para que possa ser passado o termo para busca
busca = browser.find_element_by_xpath("//*[@placeholder='Pesquisar']")

# Para mudar o modo de busca basta comentar e descomentar os modos desejados

busca.send_keys("falta de agua") # Paramentro pré definida

# busca.send_keys(sys.argv[1].strip()) # Paramentro passado por argumento

# procura = input(str('Digite o que produra: ')).strip() # Paramentro por input
# busca.send_keys(procura) # Busca o paramentro que foi passado

# Envia o termo de busca para pesquisa no site
busca.send_keys(Keys.RETURN)

# Aguarda 5 segundos para que site carregue
time.sleep(5)

# Seleciona a noticia em destaque
noticia = browser.find_element_by_xpath("//div[@class='box-noticia2 box-noticia4 first']//h2[@class='tt_capa']")

# Coleta a URL da noticia em destaque
url = noticia.find_element_by_tag_name('a').get_attribute('href')

# Abre a URL que foi coletada da noticia em destaque
browser.get(url)

# Limpa a tela do terminal
if os.name == 'nt':
    os.system('cls') 
else:
    os.system('clear')

# Coleta e mostra no terminal o titulo da materia
titulo = browser.find_element_by_class_name("titulo")
print(titulo.text)
print()

# Coleta e mostra no terminal o body da materia
materia = browser.find_elements_by_xpath("//div[@id='tamanhotexto']//p")

# Passa por todas as TAGs <p> dendo do body de conteudo 
for c in materia:
    print(c.text)


# O siste mudou a Forma de apresentação de materias mais recentes onde usava a 
# primeita TAG <p> para mostrar a localidade da materia ou nome do autor agora 
# esta sendo usada em algumas como parte da materia e outras nao aparece.

# Para visualizar materias antigas comente da linha 73 ~ 74 descomente 83 ~ 88

# suprimir = browser.find_element_by_tag_name('sup')
# oculto = suprimir.text

# for c in materia:
#         if c.text != oculto:
#             print(c.text)

print()

# Encerra o processo do browser
browser.quit()
