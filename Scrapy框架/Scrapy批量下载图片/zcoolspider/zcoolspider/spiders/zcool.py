import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Scrapy框架.Scrapy批量下载图片.zcoolspider.zcoolspider.items import ZcoolspiderItem


class ZcoolSpider(CrawlSpider):
    name = 'zcool'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/home?p=1#tab_anchor']

    rules = (
        Rule(LinkExtractor(allow=r'p=\d+#tab_anchor'), follow=True),
        Rule(LinkExtractor(allow=r'/work/.+=.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print(response.url)
        # 获取图片链接
        img_urls = response.xpath('//div[@class="photo-information-content"]/img/@src').getall()
        # 标题
        img_title = ''.join(response.xpath('//h2//text()').getall()[0]).strip()
        print(img_title)
        print(img_urls)
        item=ZcoolspiderItem(title=img_title,image_urls=img_urls)
        yield item
