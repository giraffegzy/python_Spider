from bs4 import BeautifulSoup
import requests
import pymongo
import time
from ex4_channel import channel_list
import random
"""
测试ip地址，请求头 网址 ：http://httpbin.org/ip
"""
clent = pymongo.MongoClient('localhost',27017)
ceshi =clent['ceshi']
url_list = ceshi['url_list']
info_list = ceshi['info_list']


def get_links_from(channel, pages, who_sells=0):
    link_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(link_view)
    time.sleep(random.randint(0,2))
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('div > table > tbody > tr > td.t > a'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url':item_link})
            print(item_link)
    else:
        pass

def get_detail_info(url):
    wb_data = requests.get(url)
    time.sleep(random.randint(0,4))
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles = soup.select("div.info_lubotu.clearfix > div.box_left_top > h1")
    prices = soup.select("div.info_massege.left > div.price_li > span > i")
    areas = soup.select("div.info_massege.left > div.palce_li > span > i")
    for title,price,area in zip(titles,prices,areas):
        data = {
            "title":title.get_text(),
            "price": price.get_text(),
            "area" : area.get_text(),


        }
        print(data)
        info_list.insert_one(data)

