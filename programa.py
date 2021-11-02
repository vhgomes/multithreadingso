import requests
from selenium.webdriver.chrome import options
from selenium import webdriver
import time
from urllib.parse import unquote

def downloadJsonFromSite():
    print("Gerando uma ficha...")
    url = 'https://yurialessandro.github.io/gerador-ficha-tormenta20/'
    options = webdriver.ChromeOptions()
    options.add_argument('download.default_directory=C:/Users/Usuariio/Desktop/so/jsons')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main-screen"]/div[1]/button[1]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="main-screen"]/div[3]/div[1]/div[1]/div[1]/a').click()
    time.sleep(2)

def printJsonOnTerminal():
    print("Gerando ficha para printar na tela")
    url = 'https://yurialessandro.github.io/gerador-ficha-tormenta20/'
    options = webdriver.ChromeOptions()
    options.add_argument('download.default_directory=C:/Users/Usuariio/Desktop/so/jsons/')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main-screen"]/div[1]/button[1]').click()
    time.sleep(2)
    json_xpath = browser.find_element_by_xpath('//*[@id="main-screen"]/div[3]/div[1]/div[1]/div[1]/a')
    json = json_xpath.get_attribute("href")
    json = unquote(json).replace("data:text/json;charset=utf-8,", "")
    time.sleep(1)

    # print(f'\n {unquote(json).replace("data:text/json;charset=utf-8,", "")}')


downloadJsonFromSite()
