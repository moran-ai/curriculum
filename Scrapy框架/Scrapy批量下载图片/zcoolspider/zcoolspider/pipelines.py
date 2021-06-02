# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes

from Scrapy框架.Scrapy批量下载图片.zcoolspider.zcoolspider.settings import IMAGES_STORE


class ZcoolspiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """
        获取图片链接的列表
        :param item:
        :param info:
        :return:
        """
        images_requests = super().get_media_requests(item, info)
        for image in images_requests:
            image.item = item  # 对每一个图片链接的请求都添加一个item属性
            # print(image)
        return images_requests

    # 重写该方法，自定义文件存储的路径
    # def file_path(self, request, response=None, info=None):
    #     old_path = super().file_path(request)
        # title = request.item['title'].replace(' | ', '')
        #
        # # 拼接保存的路径
        # save_path = os.path.join(IMAGES_STORE, title)
        #
        # # 提取文件名
        # image_name = old_path.replace('full/', '')
        # return os.path.join(save_path, image_name)

        # title=request.item['title']


    def file_path(self, request, response=None, info=None, *, item=None):
        title = request.item['title']
        title = ''.join(title).replace('[', '').replace(']', '')
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        # print(image_guid)
        # return f'{IMAGES_STORE}/{title}/{image_guid}.jpg'

        return f'{IMAGES_STORE}/{title}/{image_guid}.jpg'