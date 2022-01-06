import scrapy
import json

class MotorSpider(scrapy.Spider):
    name = 'motor'
    allowed_domains = ['https://www.carmax.com/cars/all']
    start_urls = ['https://www.carmax.com/cars/api/search/run?uri=%2Fcars%2Fall&skip=24&take=24&zipCode=66204&radius=90&shipping=0&sort=20&scoringProfile=segment_11&visitorID=217ae021-bb20-46c3-97cc-d680000b2cfd']

    def parse(self, response):
        data = json.loads(response.body)
        yield data
