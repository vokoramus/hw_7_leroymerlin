# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose
from .settings import PRICE_FULL_SAVING


def price_to_int(price_list):
    try:
        res = int(price_list[0].replace('\xa0', ''))
        if PRICE_FULL_SAVING:  # если цена собирается в виде кортежа (с валютой и ед.изм.)
            price_list.remove(' ')
            price_list = [res] + price_list[1:]
        else:
            price_list = res
        return price_list
    except:
        return price_list


def characteristics_to_dict(charact_list):
    ''' в поле characteristics ItemLoader передает список:
        - (первая половина списка) названия характеристик
        - (первая половина списка) значения
    Данный метод "соединяет" две половины списка, формируя словарь {"характеристика": "значение"},
    сохраняемый в поле scrapy.Field "characteristics".
    '''

    try:
        charact_dict = {}
        half_len = len(charact_list)//2
        for charact in range(half_len):
            charact_dict[charact_list[charact]] = charact_list[charact + half_len]
    except:
        return charact_list
    else:
        return charact_dict


class LeroyItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    if PRICE_FULL_SAVING:   # если цена собирается в виде кортежа (с валютой и ед.изм.)
        price = scrapy.Field(input_processor=Compose(price_to_int))
    else:
        price = scrapy.Field(input_processor=Compose(price_to_int), output_processor=TakeFirst())

    _id = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    characteristics = scrapy.Field(output_processor=Compose(characteristics_to_dict))
    photos = scrapy.Field()
