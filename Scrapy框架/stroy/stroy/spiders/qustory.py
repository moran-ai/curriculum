import scrapy


class QustorySpider(scrapy.Spider):
    name = 'qustory'
    allowed_domains = ['la']
    start_urls = ['http://www.xbiquge.la/24/24730/12077248.html']

    def parse(self, response):
        title = response.xpath("//div[@class='box_con']/div[@class='bookname']/h1/text()").extract()
        cotent = response.xpath("string(//div[@id='content'])").getall()
        # print(title)
        # print(''.join(cotent).replace('\r\r\xa0\xa0\xa0\xa0', '').strip())
        # print(cotent)
        next_url = 'http://www.xbiquge.la/24/24730/'+response.xpath("//div[@id='list']/dl/dd[3]/a/@href").extract_first()
        print(next_url)
        yield {
            'title': title,
            'cotent': cotent
        }