# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = "file:///C:/Users/Mateus/Documents/testselenium/04cursose01/index.html"

driver.get(url)
sleep(2)

lista_n_ord = driver.find_element(By.TAG_NAME,'ul')
print(lista_n_ord.find_element(By.TAG_NAME,'li').text)
x = lista_n_ord.find_elements(By.TAG_NAME,'li')
print(x[-1].text)

take = urlparse(driver.current_url)

print(take.path)



