import scrapy
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# URL que você deseja fazer crawling
url = 'http://brickset.com/sets/year-2016'

# Configuração do MongoDB
mongo_client = MongoClient('localhost', 27017)  # Estou conectando ao localhost na porta padrão
db = mongo_client['web_crawler_db'] # Estou criando um db
collection = db['web_data'] # Estou criando uma collection



class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
  
    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )


def save_to_mongodb(data):
    # Salva os dados no MongoDB
    collection.insert_one(data) # Enserindo dados na collection

# def web_crawler(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')
#             # Aqui você pode escrever o código para extrair os dados relevantes do BeautifulSoup
#             # Por exemplo, suponha que você esteja procurando por tags <p> para extrair o texto:
#             paragraphs = soup.find_all('p')
#             extracted_data = [p.get_text() for p in paragraphs]

#             # Salva os dados no MongoDB
#             save_to_mongodb({'url': url, 'data': extracted_data})
#             print(f"Dados extraídos e salvos do URL: {url}")
#         else:
#             print(f"Erro ao acessar o URL: {url}, status code: {response.status_code}")
#     except Exception as e:
#         print(f"Erro durante o crawling: {e}")

# if __name__ == "__main__":
#     web_crawler(url)
