import requests
import openai
from bs4 import BeautifulSoup
import sys
from pathlib import Path

# Obtém o diretório pai do diretório atual
diretorio_pai = str(Path(__file__).resolve().parent.parent)
sys.path.append(diretorio_pai)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from suporte import congela
from time import sleep

driver = webdriver.Chrome()

url = 'https://www.booking.com/searchresults.pt-br.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAS24ARfIAQzYAQHoAQGIAgGoAgO4AvOklakGwAIB0gIkODliMmQ1YWMtNzhhYi00M2QzLWEwOTItMzI2YTBmYmVjYzdh2AIF4AIB&sid=fed2396a63cc0c98484a0ed047b4c1a2&aid=304142&ss=Alberta&ssne=Alberta&ssne_untouched=Alberta&efdco=1&lang=pt-br&src=searchresults&dest_id=3131&dest_type=region&checkin=2023-12-02&checkout=2023-12-03&group_adults=2&no_rooms=1&group_children=0&nflt=entire_place_bedroom_count%3D2'

#Abrindo Url #1
driver.get(url)
congela(20)

#tirando cookies #2
try:
    # Aguardar até que o botão de cookies seja visível
    cookies_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="b2searchresultsPage"]/div[23]/div/div/div/div[1]/div[1]/div/button')))
    cookies_button.click()
except Exception as e:
    print(f"Erro ao clicar no botão de cookies: {e}")


dadoshoteis = driver.find_elements(By.CSS_SELECTOR,'.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4')

#Pego os titulos dos hoteis
# names = driver.find_elements(By.CSS_SELECTOR,'[data-testid="title"].f6431b446c.a15b38c233')

# for i in names:
#     print(i.text)
#     sleep(2)





# Configurar a chave da API da OpenAI
openai.api_key = "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"


# Fazer solicitação HTTP e coletar HTML
response = requests.get(url)
html = response.text

# Limitar o tamanho do contexto
context_limit = 4097
html = html[:context_limit]

# Criar um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')


# Exemplo de extração de dados: Vamos extrair todos os links da página
links = soup.find_all('a')

# Criar uma lista para armazenar os textos dos links
#textos_dos_links = [link.get_text() for link in links]
textos_dos_links = [dados.text for dados in dadoshoteis if sleep(2) is None ]


# Enviar HTML para o ChatGPT
# Enviar o texto extraído para o ChatGPT como contexto
contexto = f"Links da página: {', '.join(textos_dos_links)}" 

response_chatgpt = openai.Completion.create(
    engine="text-davinci-002",
    prompt=contexto,
    temperature=0.7,
    max_tokens=150
)

# Extrair e exibir a resposta do ChatGPT
chatgpt_output = response_chatgpt.choices[0].text
print(chatgpt_output)


###############################














