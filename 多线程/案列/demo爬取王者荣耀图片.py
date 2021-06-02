import requests
import os
from fake_useragent import UserAgent
from urllib import parse
from urllib import request

headers = {
    'User-Agent': str(UserAgent().random),
    'referer': 'https://pvp.qq.com/'
}


def send_request():
    url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1616732018322'
    resp = requests.get(url=url, headers=headers)
    # print(resp.text)
    # print(resp.json)
    return resp.json()


url_list = []


def parse_url(data):
    for i in range(1, 9):
        # 图片的url
        img_url = data['sProdImgNo_{}'.format(i)]
        # print(img_url)
        # print(img_url)
        # 对图片的url进行解码
        img_urls = parse.unquote(img_url).replace('200', '0')
        # print(img_urls)
        url_list.append(img_urls)
        return url_list


def parse_data(json_data):
    data_dict = {}
    data_list = json_data['List']
    for data in data_list:
        parse_url(data)
        #     url_list.append(img_urls)
        #     # 获取图片名字
        img_names = parse.unquote(data['sProdName'])
        data_dict[img_names] = url_list

    # for d in data_dict:
    #     print(d, data_dict[d])
    save_img(data_dict)


def save_img(d):
    for key in d:
        # print(key)
        # print(d[key])
        # 拼接路径
        dirpath = os.path.join('image', key.replace(' ', ''))
        os.mkdir(dirpath)

        # 下载图片并保存
        for index, im_url in enumerate(d[key]):
            # print(index)
            r = request.urlretrieve(im_url, os.path.join(dirpath, '{}.jpg').format(index + 1))
            print('{}下载完毕'.format(d[key][index]))
            # print(r)


def start():
    data = send_request()
    parse_data(data)
    # send_request()


if __name__ == '__main__':
    start()
