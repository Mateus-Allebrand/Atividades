#venv precisa ser ativado
#Teste com Seleniium(Sucesso na operação)

from selenium import webdriver
from selenium.webdriver.common.by import By
from func import espera

driver = webdriver.Chrome()

driver.get("https://studeo.unicesumar.edu.br/#!/access/login")
espera(10) #1


#Click cookie
driver.find_element(By.XPATH,'//*[@id="privacytools-banner-consent"]/div/div[2]/div[1]/a/div').click()
espera(10) #2

##Entrar no Studio
driver.find_element(By.XPATH,'//*[@id="username"]' ).send_keys("03896934058")
espera(10) #3
driver.find_element(By.XPATH,'//*[@id="password"]' ).send_keys("280816Mt?")
espera(20) #4
driver.find_element(By.XPATH,'//*[@id="login-form-studeo"]/div[3]/form/div[3]/div/button').click()
espera(20) #5

driver.find_element(By.XPATH,'//*[@id="modal-body"]/ui-carousel/div/div[1]/div/div[2]/div/div/button').click()
espera(10) #6

driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div[3]/div/div[3]/button').click()
espera(10) #7


driver.find_element(By.XPATH,'//*[@id="content"]/div/ui-view/ui-view/ui-view/div/div/div[2]/div/div[1]/div/ng-repeat[1]/div/div/div[3]/div/div/div/div[1]/a/span').click()
espera(10) #8













