from scrapy.crawler import CrawlerProcess  # основной класс
from scrapy.settings import Settings  # глобальный класс настроек

from leroy import settings
from leroy.spiders.leroymerlin import LeroymerlinSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)  # файл settings.py будет распарсен и передан сюда в виде объекта, похожего на словарь

    process = CrawlerProcess(settings=crawler_settings)  # обязательно нужно передать настройки

    # search = input()
    search = 'кухни'
    process.crawl(LeroymerlinSpider, search=search)  # в процесс сажаем паука

    process.start()
