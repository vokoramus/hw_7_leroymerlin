# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import re
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
# from scrapy.pipelines.files import ...
# from scrapy.pipelines.media import ...


class LeroyPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.leroy

    def process_item(self, item, spider):
        print()

        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item


class LeroyPhotosPipeline(ImagesPipeline):
    # нижеследующие методы мы просто переопределяем, а не создаем заново
    def get_media_requests(self, item, info):  # точка входа класса ImagesPipeline
        if item['photos']:
            for photo in item['photos']:
                try:
                    yield scrapy.Request(photo)  # создание новой сессии (в отличие от response в методе parse паука), аналогичный метод работает при начальном запросе в файле паука
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        path_standard = super().file_path(request, response, info)

            # folder_name
        p = re.compile(r'\/([^\/]+)\/$')
        m = p.search(item['url'])
        folder_name = m.group(1)

        p = re.compile(r'(\d+)$')
        m = p.search(folder_name)
        article = m.group(1)

        path_new = '/'.join([folder_name, path_standard[5:]])
        print()
        return path_new
