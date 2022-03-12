# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose

def price_to_int(price_list):
    try:
        res = int(price_list[0].replace('\xa0', ''))
        if len(price_list) > 1:  # если цена собирается в виде кортежа (с валютой и ед.изм.)
            price_list.remove(' ')
            price_list = [res] + price_list[1:]
        else:
            price_list = res
        # print(price_list)
        # print()
        return price_list
    except:
        return price_list


class LeroyItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(price_to_int))
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    characteristics_names = scrapy.Field()
    characteristics_values = scrapy.Field()

    _id = scrapy.Field()
