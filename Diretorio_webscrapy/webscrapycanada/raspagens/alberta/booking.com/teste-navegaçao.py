from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o navegador
driver = webdriver.Chrome()  # Ou o navegador de sua escolha

# Navegar para a página principal
url = "https://www.booking.com/"
driver.get(url)

# Encontrar e clicar no link ou botão do apartamento na página principal
apartamento_link = driver.find_element(By.XPATH, "//seu/xpath/aqui")
apartamento_link.click()

# Colher informações relevantes na página do apartamento
# Aqui você colocaria código para coletar as informações que você precisa

# Voltar para a página principal
driver.back()

# Repetir o processo para outros apartamentos
# ...

# Fechar o navegador
driver.quit()

############################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ... (código anterior)

#tirando cookies #2
try:
    # Aguardar até que o botão de cookies seja visível
    cookies_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[23]/div/div/div/div[1]/div[1]/div/button'))
    )
    cookies_button.click()
except Exception as e:
    print(f"Erro ao clicar no botão de cookies: {e}")

# ... (restante do código)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ... (seu código para iniciar o driver e outras configurações)

url = 'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIAQzYAQHoAQGIAgGoAgO4AvOklakGwAIB0gIkODliMmQ1YWMtNzhhYi00M2QzLWEwOTItMzI2YTBmYmVjYzdh2AIF4AIB&sid=fed2396a63cc0c98484a0ed047b4c1a2&aid=304142&ss=Alberta&ssne=Alberta&ssne_untouched=Alberta&efdco=1&lang=pt-br&src=searchresults&dest_id=3131&dest_type=region&checkin=2023-12-02&checkout=2023-12-03&group_adults=2&no_rooms=1&group_children=0&nflt=entire_place_bedroom_count%3D2'

# Abrindo Url
driver.get(url)

# Localizando todos os links para os detalhes dos apartamentos
links_apartamentos = driver.find_elements(By.XPATH, '//seu/xpath/para/links/dos/apartamentos')

# Iterando sobre os links dos apartamentos
for link_apartamento in links_apartamentos:
    # Clicando no link para os detalhes do apartamento
    link_apartamento.click()

    # Aguardando até que a página de detalhes do apartamento seja carregada
    WebDriverWait(driver, 10).until(EC.url_contains('/detalhes-do-apartamento/'))

    # Colhendo informações do apartamento
    # ... (seu código para coletar informações)

    # Voltando para a página anterior (lista de apartamentos)
    driver.execute_script("window.history.go(-1)")

    # Aguardando até que a página anterior seja carregada
    WebDriverWait(driver, 10).until(EC.url_contains('/searchresults/'))

# Fechando o navegador no final
driver.quit()
