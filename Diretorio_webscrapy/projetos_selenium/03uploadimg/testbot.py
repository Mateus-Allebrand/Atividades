from selenium import webdriver
from selenium.webdriver.common.by import By
from suportes import espera



driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

#Nesse trecho do codigo consegui fazer o upload de uma imagem 
driver.find_element(By.XPATH,'//*[@id="file-upload"]').send_keys("C:\\Users\\Mateus\\Documents\\testselenium\\testcasosobserv\\gatotest.jpg")
espera()

#Nesse trecho do codigo achei o botão de enviar e enviei(submit)
driver.find_element(By.ID,"file-submit").submit()
espera()

#Aqui estou verificando se o texto "File Uploaded!" esta presente no html da pagina
if "File Uploaded!" in driver.page_source:
    print("File upload success")
else:
    print("File upload not successful")
espera()

driver.quit()

