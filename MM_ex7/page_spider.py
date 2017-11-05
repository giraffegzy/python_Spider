import time
import re
import urllib
import requests
import random

from urllib import request
from bs4 import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost',27017)
jiandan = client['jiandan']
img_info = jiandan['img_info']

# 获得图片url
def get_img_url(url):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
    wb_data = requests.get(url,headers=headers)
    time.sleep(random.randint(0,4))
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    rzc = r'w\w*\d\.\w*\.\w*/large/\w*\.\w*'
    image = re.compile(rzc)
    results = re.findall(image,str(soup))
    #print(results)
    for url in results:
        print(url)
        data = {
            'img_url':url,
        }
        img_info.insert_one(data)

def get_Db_url():
    for info in img_info.find():
        url = info['img_url']
        yield url

def save_imgs(index,url,filepath='./img/'):
    if 'jpg' in url:
        filename = '{}{}'.format(filepath, '{}'.format('%s.jpg')% index)
    else:
        filename = '{}{}'.format(filepath, '{}'.format('%s.gif')% index)
    try:
        urllib.request.urlretrieve('http://'+url, filename)
        print("第{}张图片".format(index))
    except urllib.request.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        urllib.request.urlretrieve('http://'+url, filename)
        print("第{}张图片".format(index))


if __name__ == '__main__':
    for num in range(1,100):
        url= 'http://jandan.net/ooxx/page-{}#comments'.format(num)
        get_img_url(url)
    for url,index in zip(range(1,img_info.count()+1),get_Db_url()):
        save_imgs(url,index)


