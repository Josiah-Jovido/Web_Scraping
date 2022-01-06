import scrapy

class CarSpider(scrapy.Spider):
    name = 'cars'
    start_urls = ['https://www.carmax.com/cars/all']

    def parse(self, response):
        for products in response.css('.car-tile'):
                yield {
                    'name': products.css('span.year-make::text').get(),
                    'model': products.css('span.model-trim::text').get(),
                    'price': products.css('span.price::text').get(),
                    'link': products.css('div.orig').attrib['href'],
                    'image': products.css('img.loaded').attrib['src'],
                    'distance': products.css('span.miles::text').get(),
                    'availability': products.css('span.transfer::text').get(),
                    'key features': products.css('div.car-features::text').get(),
                    'location': products.css('.car-tile--extra-content div:nth-child(3)::text').get(),
                    'description': products.css('.car-tile--extra-content div:nth-child(4)::text').get(),
                    'transmission': products.css('.car-tile--extra-content div:nth-child(5)::text')[1].get(),
                    'exterior color': products.css('.car-tile--extra-content div:nth-child(5)::text')[2].get(),
                    'interior color': products.css('.car-tile--extra-content div:nth-child(5)::text')[3].get(),
                    'Vechicle info': products.css('script::text').get()
                }
