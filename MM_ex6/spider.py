import re
import requests
import json
from urllib import request
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib.request
import random
import time


client = MongoClient('localhost',27017)
jinri = client['jinri']
images_list = jinri['images_list']
info_list = jinri['info_list']


# 获取图集url
def get_index_list(url):
    with request.urlopen(url) as res:
        time.sleep(random.randint(0,4))
        wb_data = json.loads(res.read().decode())
        wb_data = wb_data.get('data')
        # print(wb_data)
        urls = [index_url.get('article_url') for index_url in wb_data if index_url.get('article_url')]
        titles = [title.get('title') for title in wb_data if title.get('title')]
        for index_url,title in zip(urls,titles):
            data = {
                'index_url':index_url,
                'title':title,
            }
            print(data)
            images_list.insert_one(data)


# 获取图片url
def get_imges(url):
    wb_data = requests.get(url)
    time.sleep(random.randint(0,2))
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    rzc = r'\"url\":\"(.+?)\"'
    image = re.compile(rzc)
    result = re.findall(image, str(soup))
    # print(result)
    for url in result :
        if 'http:' in url:
            if '/pb9'in url:
                url_0 = url.split('\\')[0]
                url_1 = url.split('\\')[1]
                url_2 = url.split('\\')[2]
                url_3 = url.split('\\')[3]
                url_4 = url.split('\\')[4]
                hou = '.png'
                data = {
                    'url':str(url_0+url_1+url_2+url_3+url_4+hou)
                }
                info_list.insert_one(data)
                print(data)


# 取出index_url
def get_index_url():
    for url in images_list.find():
        url_image = url['index_url']
        yield url_image


# 保存在本地
def get_image_info():
    for info in info_list.find():
        url = info['url']
        yield url


def save_imgs(index,url,filepath='./img/'):
        filename = '{}{}'.format(filepath,'%s.jpg'%index)
        urllib.request.urlretrieve(url,filename)
        print("第{}张图片".format(index))


if __name__ == '__main__':
    for i in range(0,140,20):
        url = 'https://www.toutiao.com/search_content/?offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=3'.format(i)
        get_index_list(url)
    for url in get_index_url():
        get_imges(url)

    for index,url in zip(range(1,info_list.count()+1),get_image_info()):
        if 'tuchong' in url: # 因为发现tuchong是个错误url
            print("404 Not Found")
        else:
            save_imgs(index,url)



