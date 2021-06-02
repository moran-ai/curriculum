# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StroyPipeline:
    def open_spider(self, spider):
        self.file = open('小说.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        inf = ''.join(item['cotent']).replace('    ', '').replace('\r', '')
        info = ''.join(item['title']) + '\n' + inf
        n = info + inf
        self.file.write(n)
        return item

    def close_spider(self, spier):
        self.file.close()
