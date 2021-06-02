import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Scrapy框架.scrapy爬取猎聘网职位信息.job.job.items import JobItem


class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://www.liepin.com/a/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/zhaopin/.+curPage=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 职位名称
        title =  response.css('.title-info h1::text').get()
        # 公司名称
        company = response.css('.company-logo p a::text').get()
        # 任职要求
        job_qualifications = response.css('.job-qualifications span::text').getall()
        # 职位描述
        job_desc_list = response.css(".content.content-word::text").getall()
        job_desc = ''.join(job_desc_list).strip()
        # 工作地点
        city = response.css(".basic-infor span a::text").get()

        item = JobItem(title=title, company=company, job_qualifications=job_qualifications, job_desc=job_desc,
                       city=city)
        yield item
