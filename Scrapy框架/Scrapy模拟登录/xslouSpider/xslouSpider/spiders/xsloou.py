import scrapy


class XsloouSpider(scrapy.Spider):
    name = 'xsloou'
    allowed_domains = ['com']

    # start_urls = ['http://com/']

    def start_requests(self):
        url = '登录页面url'
        form_data = {
            '登录页面的数据'
        }
        yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        '''
        登录成功后执行的操作
        :param response:
        :return:
        '''
        pass
