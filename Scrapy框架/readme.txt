1.安装
    pip install scrapy
2.创建Crawl爬虫
    scrapy genspider -t crawl 爬虫名 域名

解析方式
    xpath
            extract()
            extract_first()  不能用于Selector对象
            getall()
            get()

异步保存MySQL数据
步骤：
    ① 编写配置文件
    ② 读取配置文件
    ③ 创建数据库 (navicat的使用)
    ④ 使用twisted.enterprise.adbapi创建连接池
    ⑤ 使用runInteraction来运行插入语句的函数
    ⑥ 使用cursor对象，来执行sql语句，cursor对象位于插入语句函数的第一个非self参数位置

Scrapy模拟登录
    scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse)
        url:登录页面url
        formdata:登录需要的数据
        callback:回调函数，登录成功需要执行的操作

Scrapy批量下载图片
    from scrapy.pipelines.images import ImagesPipeline
    ITEM_PIPELINES = {
    # 'zcoolspider.pipelines.ZcoolspiderPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 300
                        }