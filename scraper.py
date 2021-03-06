from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from time import sleep
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # pylint: disable=no-member
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def convertArray(url):
    url = "https://quizlet.com/"+url.split("/",4)[3]+"/print/"
    driver = webdriver.Chrome(resource_path('chromedriver'))
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('PrintPageOptions-radioWrap'))
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div[4]/label/input').click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('PrintPageOptions-radioWrap'))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    firstCol = soup.find_all(class_='term inner')
    secondCol = soup.find_all(class_ = 'def inner')
    if len(firstCol) == 0:
        sleep(2)
        firstCol = soup.find_all(class_='term inner')
        secondCol = soup.find_all(class_ = 'def inner')
    terms = []
    definitions = []

    for term in firstCol:
        terms.append(term.text.split(".",1)[1])
    for definition in secondCol:
        definitions.append(definition.text)

    data = {'Terms':terms,'Definitions':definitions}
    df = pd.DataFrame(data, columns=['Terms', 'Definitions'])
    return df