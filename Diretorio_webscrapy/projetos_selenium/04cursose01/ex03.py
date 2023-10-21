# Desafio concluído com sucesso
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = "https://selenium.dunossauro.live/exercicio_03.html"

driver.get(url)
sleep(2)

#primeiro click
driver.find_element(By.XPATH,'//*[@id="main"]/li/a').click()
sleep(5)

#respondendo a primeira questão
respcerta1 = driver.find_element(By.XPATH,'//*[@id="main"]/li[1]/a').click()
sleep(8)

#respondendo a segunda questão
respcerta2 = driver.find_element(By.XPATH,'//*[@id="main"]/li[1]/a').click()
sleep(4)

#respondendo a terceira questão
respcerta3 = driver.find_elements(By.TAG_NAME,'a')

print(respcerta3[5].text)
respcerta3[5].click()
sleep(8)
driver.refresh()
sleep(3)





# 0 Olar Jovis :)
# 1 Youtube
# 2 Apoia.se
# 3 Curso
# 4 CDC
# 5 page_3.html
# 6 bage_3.html