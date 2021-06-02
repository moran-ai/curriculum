import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    rules = (
        Rule(LinkExtractor(allow=r'article/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/text/page/\d+/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='article-title']/text").get()
        print(title)
        print(response.url)
