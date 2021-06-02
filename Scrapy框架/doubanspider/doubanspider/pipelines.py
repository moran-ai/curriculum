# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 存储到excel文件中
import openpyxl


class DoubanspiderPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active  # 获取活动表
        self.ws.append(['书名', '出版社', '评分'])

    def process_item(self, item, spider):
        line = [item['title'], item['publish'], item['score']]
        # 将数据添加到工作表中
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('book.xlsx')
        self.wb.close()
