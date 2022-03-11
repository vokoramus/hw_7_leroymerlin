import scrapy


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://spb.leroymerlin.ru/search/?q=кухни']

    def parse(self, response):
        pass
