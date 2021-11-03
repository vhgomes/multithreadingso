from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import time, threading

def downloadJsonFromSite():
    print("Gerando uma ficha...")
    url = 'https://yurialessandro.github.io/gerador-ficha-tormenta20/'
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\Usuariio\Desktop\so\jsons",  #Professor, colocar um path para um local aonde o senhor deseja.
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })
    options.set_headless(headless=True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="main-screen"]/div[1]/button[1]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="main-screen"]/div[3]/div[1]/div[1]/div[1]/a').click()
    print("Completo - Ficha Gerada e Baixada")
    time.sleep(2)
    browser.quit

def menu():
    print("ANTES DE RODAR O PROGRAMA, ESCOLHER UM PATH AONDE SERA BAIXADO O ARQUIVO")
    print("________________________________________________")
    print('|Gerador de JSON de fichas de RPG | Tormenta 20|')
    print("------------------------------------------------")

menu()
for i in range(5):
    browserThread = threading.Thread(target=downloadJsonFromSite)
    browserThread.start()

