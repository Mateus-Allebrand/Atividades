from selenium import webdriver
from suport import congela_tempo
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Chrome()

# url = "file:///C:/Users/Mateus/Documents/testselenium/04cursose/aula03.html"

# driver.get(url)

marca = time.time()



driver = webdriver.Chrome()

url = "file:///C:/Users/Mateus/Documents/testselenium/04cursose/render/index.html"

driver.get(url)
congela_tempo(t=7)

paragrafos = []

while True:
    
    if "Fim da linha" not in driver.page_source:
        a = driver.find_element(By.TAG_NAME,'a').click()
        congela_tempo(t=7)

    if "Fim da linha" in driver.page_source:
        pa = driver.find_elements(By.TAG_NAME,'p')
        for i in pa:
            paragrafos.append(i.text)
        congela_tempo(t=2)
        break


print(paragrafos)

  
    


