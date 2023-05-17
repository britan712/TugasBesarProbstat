import scrapy
import pandas as pd

class ZillowSpider(scrapy.Spider):
    name = "zillow"

    def start_requests(self):
        url = "https://www.zillow.com/homes/"
        filters = {
            'country': 'Brazil'
        }
        yield scrapy.FormRequest(url=url, formdata=filters, callback=self.parse)

    def parse(self, response):
        cities = response.css('div.search-page-list-container li')
        
        data = []

        count = 0

        for city in cities:
            city_name = city.css('h4 a::text').get().strip()
            num_homes = city.css('div h6 span::text').get().strip()

            data.append({'City': city_name, 'Num Homes': num_homes})

            count += 1
            if count >= 40:
                break

        df = pd.DataFrame(data)
        df.to_excel('databrazil.xlsx', index=False)
