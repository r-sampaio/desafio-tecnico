#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

banco = create_engine('sqlite:///db.sqlite3')

Session = sessionmaker(bind=banco)

body_page = declarative_base()

class ConteudoPage(body_page):
    
    __tablename__ = 'ConteudoPage'
    
    id = Column(Integer, primary_key=True)
    titulo = Column('titulo', String(200))
    body = Column('body', String(2000))

    def __init__(self, titulo, body):
        self.titulo = titulo
        self.body = body

body_page.metadata.create_all(banco)
session = Session()
tabela = ConteudoPage(titulo=None, body=None)

chrome_options = Options()

def limpa():
    # Limpa a tela do terminal
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def end_process():
    if os.name == 'nt':
        os.system('taskkill /F /IM chrome.exe')
    else:
        try:
            os.system('killall -9 chrome')
        except:
            os.system('killall -9 google-chrome-stable')


def processando():
    print('\033[34mProcessando...\033[m')


def google(headless, excludeSwitches, maximized):
    if headless:
        # Executa o browser em background mostrando as informações no terminal
        chrome_options.add_argument("--headless") # Para desativar, comente essa linha
    
    if excludeSwitches:
        # Desativa as mensagem de erro e infomações no terminal
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if maximized:
        chrome_options.add_argument("--start-maximized")


limpa()

conexao = input(str('Deseja abrir o navegador? [S/N]: ')).strip()[0]
if conexao in 'sS':
    headless = False
    janela = input(str('Deseja maximizar a janela? [S/N]: ')).strip()[0]
    if janela in 'sS':
        maximized = True
    elif janela in 'nN':
        maximized = False
elif conexao in 'nN':
    headless = True
    maximized = False


avisos = input(str('Deseja exibir aviso/erros no terminal? [S/N]: ')).strip()[0]
if avisos in 'sS':
    excludeSwitches = False
elif avisos in 'nN':
    excludeSwitches = True

encerra = input(str('Deseja encerrar o navegador? [S/N]: '))

procura = input(str('Digite o que produra: ')).strip() # Paramentro por input
if procura == '':
    procura = 'falta de agua'

google(headless, excludeSwitches, maximized)

# Cria a instancia com os paramentos passados para o browser e o caminho do driver Google
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")

limpa()
processando()


# Abre o browser no site passado por paramentro
browser.get("https://www.acordacidade.com.br")


# Aguarda 5 segundos para que site carregue
time.sleep(5)


# Clica na lupa para que o campo de busca apareça
lupa = browser.find_element_by_xpath("//div[@class='busca']").click()

# Seleciona o campo para que possa ser passado o termo para busca
busca = browser.find_element_by_xpath("//*[@placeholder='Pesquisar']")


# Busca o paramentro que foi passado
busca.send_keys(procura)


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

limpa()

# Coleta e mostra no terminal o titulo da materia
titulo = browser.find_element_by_class_name("titulo")
if conexao in 'nN':
    tabela.titulo = titulo.text
    # print(titulo.text)
    # print()

# Coleta e mostra no terminal o body da materia
materia = browser.find_elements_by_xpath("//div[@id='tamanhotexto']//p")

if conexao in 'nN':
    conteudo = []
    # Passa por todas as TAGs <p> dendo do body de conteudo 
    for c in materia:
        conteudo.append(c.text)
    tabela.body = (' '.join(conteudo))
    # print()

session.add(tabela)
session.commit()

dados = session.query(ConteudoPage).all()
for conteudo_page in dados:
    print(f'{conteudo_page.titulo}\n\n{conteudo_page.body}')

body_page.metadata.drop_all(banco)
session.close()

# Encerra o processo do browser
if encerra in 'sS':
    browser.quit()

# end_process()
