from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,time 
from suport import congela
import csv


#Entrando site
url = 'https://www.booking.com/searchresults.pt-br.html?ss=canada&ssne=Canasvieiras&ssne_untouched=Canasvieiras&label=msn-gK1UDBc2qZ3A4RJKWN3DcA-79852220055878%2525253Atikwd-79852393959906%2525253Aloc-20%2525253Aneo%2525253Amte%2525253Alp147508%2525253Adec%2525253Aqsbooking.com&aid=2369661&lang=pt-br&sb=1&src_elem=sb&src=searchresults&dest_id=-574890&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=xb&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=54a176a8573f0059&ac_meta=GhA1NGExNzZhODU3M2YwMDU5IAAoATICeGI6BmNhbmFkYUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0'

driver = webdriver.Chrome()

driver.get(url)
congela(23)



#removendo a mensagem de login
log = driver.find_element(By.XPATH,'//*[@id="b2searchresultsPage"]/div[22]/div/div/div/div[1]/div[1]/div/button').click()
congela()


titulos = driver.find_elements(By.CSS_SELECTOR,'[data-testid="title"].f6431b446c.a15b38c233')
congela(15)

notas = driver.find_elements(By.CSS_SELECTOR,'.a3b8729ab1.d86cee9b25')
congela(15)

avaliacoes = zip(titulos,notas)
    

resumo = {}

for t,n in avaliacoes:
    resumo[t.text] = n.text


with open("hoteis-notas.csv", "a",newline='') as arquivo:

    escritor = csv.writer(arquivo)

    for nhotel,ahotel in resumo.items():
        escritor.writerow([nhotel,ahotel])
        


    
