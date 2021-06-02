# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from twisted.enterprise import adbapi


class LieyunspiserPipeline:
    def __init__(self, mysql_config):
        """
        构建数据库连接池
        :param mysql_config:
        """
        self.dbpool=adbapi.ConnectionPool(
            mysql_config['DRIVER'],
            host=mysql_config['HOST'],
            user=mysql_config['USER'],
            password=mysql_config['PASSWORD'],
            database=mysql_config['DATABASE']
        )

    @classmethod
    def from_crawler(cls, crawler):
        """
        重写该方法，以后创建对象时，会调用该方法获取pipline对象
        :param crawler:
        :return:
        """
        mysql_config = crawler.settings['MYSQL_DB_CONFIG']
        return cls(mysql_config)

    def inser_item(self, cursor, item):
        """
        插入数据
        :param cursor:
        :param item:
        :return:
        """
        sql = 'insert into article (id,title,time,author, content,atircle_url) values (null, %s,%s,%s,%s,%s)'
        args = (item['title'], item['time'], item['author'], item['content'], item['atricle_url'])
        cursor.execute(sql, args)

    def process_item(self, item, spider):
        """
        执行数据插入的函数
        :param item:
        :param spider:
        :return:
        """
        result=self.dbpool.runInteraction(self.inser_item, item)
        # 数据插入如果出错，调用的函数  inser_error
        result.addErrback(self.inser_error)
        return item

    def inser_error(self,failure):
        """
        插入数据错误方法
        :return:
        """
        print('==========================')
        print(failure)
        print('==========================')