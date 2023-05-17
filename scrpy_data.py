import scrapy
import pandas as pd

class ZillowSpider(scrapy.Spider):
    name = "zillow"

    def start_requests(self):
        url = "https://www.zillow.com/homes/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        listings = response.css('div.list-card-info')

        data = []

        count = 0

        for listing in listings:
            area = listing.css('div.list-card-details::text').get().strip()
            price = listing.css('div.list-card-price::text').get().strip()

            data.append({'Area': area, 'Price': price})

            count += 1
            if count >= 40:
                break

        df = pd.DataFrame(data)
        df.to_excel('datasaya.xlsx', index=False)
