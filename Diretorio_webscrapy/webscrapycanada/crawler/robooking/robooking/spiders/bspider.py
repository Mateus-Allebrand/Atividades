from pathlib import Path
import json
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "robook"

    start_urls = [
            "https://www.booking.com/searchresults.en-gb.html?ss=Toronto&ssne=Toronto&ssne_untouched=Toronto&sid=f3aa26bd8064dbd9fe7a4eef6f2a1c5c&aid=7342726&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-574890&dest_type=city&checkin=2023-12-02&checkout=2023-12-03&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
        ]
        
       
    def parse(self, response):
        # Imprima o conteúdo HTML para verificar se está obtendo os dados corretos
        print(response.body)

        data = []

        hotel_names = response.css('div[data-testid="title"].f6431b446c.a15b38c233::text').get()

    
        yield {"namehotel": hotel_names}



        # Save the output to a JSON file
        self.save_to_json(data)

    def save_to_json(self, data):
        with open("output.json", "w") as f:
            f.write(json.dumps(data, indent=2))
        self.log("Saved data to output.json")




    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"output.html"

    #     # Save HTML content to a file
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    #     self.log(f"Saved file {filename}")
