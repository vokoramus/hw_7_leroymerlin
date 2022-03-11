import scrapy
from scrapy.http import HtmlResponse
from leroy.items import LeroyItem
from scrapy.loader import ItemLoader


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://spb.leroymerlin.ru/search/?q={kwargs.get("search")}']

    def parse(self, response: HtmlResponse):
        links = response.xpath('//div[@data-qa-product]/a')
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyItem(), response=response)
        loader.add_xpath('name', '//h1/span/text()')
        loader.add_xpath('price', '//div[@data-testid="prices_mf-pdp"]//span/text()')  # [цена, валюта, ед.изм.]
        # loader.add_xpath('price', '//div[@data-testid="prices_mf-pdp"]//span[@slot="price"]')  # просто цена
        loader.add_value('url', response.url)
        loader.add_xpath('photos', '//picture[@slot="pictures"]/source[1]/@srcset')

        # loader.add_xpath('characteristics', '//picture[@slot="pictures"]/source[1]/@srcset')
        # //section[@id="characteristics"]//dl/div/dt/text()        # Характеристики
        # //section[@id="characteristics"]//dl/div/dd/text()        # Значения

        yield loader.load_item()
