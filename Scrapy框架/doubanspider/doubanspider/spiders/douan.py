# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from Scrapy框架.doubanspider.doubanspider.items import DoubanspiderItem


class DouanSpider(scrapy.Spider):
    name = 'douan'
    allowed_domains = ['com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        tr_tag = soup.find_all('tr', class_='item')
        for tr in tr_tag:
            item = DoubanspiderItem()
            title = tr.find_all('a')[1]['title']
            publish = tr.find('p', class_='pl').text
            score = tr.find('span', class_="rating_nums").text
            item['title'] = title
            item['publish'] = publish
            item['score'] = score
            print(title, '--->', publish, '--->', score)

            # 提交给引擎
            # yield item