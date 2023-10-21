#Objetivo Entrar no site da magazine e fazer download planilha financeira
#Operação Bem Sucedida

from selenium import webdriver
from selenium.webdriver.common.by import By
from suporte import espera

driver = webdriver.Chrome()


driver.get("https://ri.magazineluiza.com.br")
espera()

#cookie(Até aqui Sucesso)
driver.find_element(By.XPATH,'//*[@id="Form1"]/div[7]/a').click()
espera(20)

#Aba(Até aqui sucesso)
driver.find_element(By.XPATH,'//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
espera(15)


#informação financeira
driver.find_element(By.XPATH, '//*[@id="heading-mobile-3"]/button').click()
espera()

#Planilha de resultado
driver.find_element(By.XPATH,'//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
espera()

#planilha resultado do trimestre
driver.find_element(By.XPATH,'//*[@id="NS503pmpo+N63mNM4SoDKw=="]').click()
espera(15)


driver.quit()