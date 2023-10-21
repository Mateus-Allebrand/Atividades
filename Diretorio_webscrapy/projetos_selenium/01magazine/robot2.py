#Aqui esta uma versão melhorada do Script robot

from selenium import webdriver
from selenium.webdriver.common.by import By
from suporte import espera

driver = webdriver.Chrome()

driver.get("https://ri.magazineluiza.com.br")

xpaths = ['//*[@id="Form1"]/div[7]/a',
          '//*[@id="Form1"]/header/div/div/div/div[1]/button',
          '//*[@id="heading-mobile-3"]/button',
          '//*[@id="collapse-mobile-3"]/div/ul/li[2]/a',
          '//*[@id="NS503pmpo+N63mNM4SoDKw=="]']

for i in xpaths:
    driver.find_element(By.XPATH,i).click()
    espera()

driver.quit()