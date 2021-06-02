import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Scrapy框架.CrawlSpider.lieyunSpiser.lieyunSpiser.items import LieyunspiserItem


class LieyunSpider(CrawlSpider):
    name = 'lieyun'
    allowed_domains = ['com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        # follow=True 是否跟进
        Rule(LinkExtractor(allow=r'latest/p\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'archives/\d+'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        item = LieyunspiserItem()
        """
        解析数据
        :param response:
        :return:
        """
        # 标题
        title = ''.join(response.xpath("//h1[@class='lyw-article-title-inner']/text()").getall()).replace('\r\n', '')
        # 时间
        time = ''.join(response.xpath("//h1[@class='lyw-article-title-inner']//text()").getall()).replace('\r\n', '').strip()
        # 作者
        author = response.xpath(
            "//div[@class='author-info']/a[@class='author-name open_reporter_box']//text()").getall()
        # print(author)
        # 信息
        xinxi = response.xpath("//div[@class='author-info']/div[@class='author-sign']//text()").getall()
        # print(xinxi)
        # 内容
        content = ''.join(response.xpath('//div[@class="main-text"]//text()').getall()).replace('\r\n', '').strip()
        # print(content)
        article_url = response.url
        item['title'] = title
        item['time'] = time
        item['author'] = author
        item['content'] = content
        item['atricle_url'] = article_url
        # print(item)
        # print(title)
        yield item

