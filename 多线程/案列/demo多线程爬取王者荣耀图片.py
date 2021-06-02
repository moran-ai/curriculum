import os
import requests
import threading
from fake_useragent import UserAgent
from queue import Queue
from urllib import parse, request

headers = {
    'User-Agent': str(UserAgent().random),
    'referer': 'https://pvp.qq.com/'
}


def parse_url(data):
    """
    解析url
    :param data:
    :return:
    """
    url_list = []
    for i in range(1, 9):
        # 图片的url
        img_url = data['sProdImgNo_{}'.format(i)]
        # 对图片的url进行解码
        img_urls = parse.unquote(img_url).replace('200', '0')
        url_list.append(img_urls)
    return url_list


# 生产者线程
class Produter(threading.Thread):
    """
    获取url，发送请求，生产图片url
    """

    def __init__(self, page_queue, img_url_queue):
        super().__init__()
        self.page_queue = page_queue
        self.img_url_queue = img_url_queue

    def run(self):
        while not self.page_queue.empty():
            # 获取页数url
            page_url = self.page_queue.get()
            # 发送请求
            resp = requests.get(url=page_url, headers=headers)
            # 返回的数据
            json_data = resp.json()
            d = {}
            data_list = json_data['List']
            for data in data_list:
                l = parse_url(data)
                img_names = parse.unquote(data['sProdName'])
                d[img_names] = l
            # 文件的保存
            for key in d:
                # print(d[key])
                # 拼接路径  图片的路径
                dirpath = os.path.join('image', key.replace(' ', ''))
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)

                # 获取图片url
                for index, im_url in enumerate(d[key]):
                    # 生产图片的url，放入图片url队列中
                    self.img_url_queue.put(
                        {'image_path': os.path.join(dirpath, '{}.jpg').format(index + 1), 'image_url': im_url})


# 消费者线程
class Cumtoser(threading.Thread):
    """
    执行保存图片
    """

    def __init__(self, img_url_queue):
        # 继承父类
        super().__init__()
        # 消费者从生产者中拿url
        self.img_url_queue = img_url_queue

    def run(self):
        while True:
            try:
                # 如果20秒内还没有url，则会终止程序
                image_obj = self.img_url_queue.get(timeout=20)
                # 将图片下载到本地  参数一：url  参数二：保存的路径
                request.urlretrieve(image_obj['image_url'], image_obj['image_path'])
                print(f'{image_obj["image_path"]}下载完成')
            except:
                break


def start():
    # 创建队列
    page_queue = Queue(22)  # url页数队列
    img_url_queue = Queue(1000)  # 图片url的队列
    # 21页的数据
    for i in range(0, 22):
        page_url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={i}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1616732018322'
        # print(page_url)
        # 将url放进队列中
        page_queue.put(page_url)

    # 5个创建生产者线程对象
    for _ in range(5):
        production = Produter(page_queue, img_url_queue)
        production.start()

    # 10个消费者线程
    for _ in range(10):
        cumster = Cumtoser(img_url_queue)
        cumster.start()


if __name__ == '__main__':
    start()
