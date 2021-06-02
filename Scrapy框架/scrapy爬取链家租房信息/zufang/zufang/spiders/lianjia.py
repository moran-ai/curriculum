import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://cs.lianjia.com/zufang/pg{i}/#contentList' for i in range(1, 3)]

    def parse(self, response):
        full_url = ['https://cs.lianjia.com' + url for url in response.xpath(
            "//div[@class='content__list--item--main']/p[@class='content__list--item--title']/a[@class='twoline']/@href").getall()]
        # print(full_url)
        # print(len(full_url))
        for item in full_url:
            yield scrapy.Request(url=item, callback=self.parse_info)

    def parse_info(self, response):
        title = response.xpath("//div[1]/div[@class='content clear w1150']/p[@class='content__title']//text()").get()
        total_price = response.xpath(
            "//div[@class='content__aside--title']/span|//div[@class='content clear w1150']/div[@class='content__core']/div[@id='aside']/div[@class='content__aside--title']/text()").getall()
        price = ''.join(total_price).replace('\n', '').strip().replace('<span>', '').replace('</span>', '').replace(' ',
                                                                                                                    '')
        # print(title,price)
        # 租赁方式
        mode = response.xpath("//ul[@class='content__aside__list']/li[1]/text()").get()
        # 房屋类型
        type = response.xpath("//ul[@class='content__aside__list']/li[2]/text()").get()
        # 楼层信息
        direction = response.xpath("//ul[@class='content__aside__list']/li[3]/text()").get()
        # 电梯
        elevator = response.xpath("//div[@id='info']/ul[1]/li[9]/text()").get()
        # 车位
        parking = response.xpath("//div[@id='info']/ul[1]/li[11]/text()").get()
        # 水
        water = response.xpath("//div[@id='info']/ul[1]/li[12]/text()").get()
        # 用电
        electric = response.xpath("//div[@id='info']/ul[1]/li[14]/text()").get()
        # 燃气
        heating = response.xpath("//div[@id='info']/ul[1]/li[15]/text()").get()
        yield {
            'title': title,
            'price': price,
            'mode': mode,
            'type': type,
            'direction': direction,
            'elevator': elevator,
            'parking': parking,
            'water': water,
            'electric': electric,
            'heating': heating
        }
