#!user/bin/python
# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time

"""
获取转转商品的详情信息
包括：标题，价格，分类，区域，浏览次数

"""
def get_detail_info(url):
    wb_data = requests.get(url)
    if wb_data.status_code == 200:
        soup = BeautifulSoup(wb_data.text, 'lxml')

        title_list = soup.select('div.box_left_top > h1')
        title = title_list[0].get_text()
        prices_list =soup.select('div.price_li > span.price_now > i')
        price = prices_list[0].get_text()
        cate_list = soup.select('span.crb_i > a')
        cate = cate_list[-1].text.strip()
        area_list = soup.select('div.palce_li > span > i')
        area = area_list[0].get_text()
        view_list =soup.select('div.box_left_top > p > span.look_time')
        view = view_list[0].get_text()

        data = {
            "title":title,
            "price": price,
            "cate": cate,
            "area":area,
            "view":view,
        }
        print(data)


# 获取一页所以转转商品的信息
def get_one_page(url):
    wb_data = requests.get(url)
    if wb_data.status_code == 200:
        soup =BeautifulSoup(wb_data.text, 'lxml')
        links =soup.select(' tbody > tr.zzinfo > td.t > a.t')
        for link in links:
            href = link.get("href")
            if "zhuanzhuan" in href:
                get_detail_info(href)


def get_next_page(star,end):
    for i in range(star,end):
        url = 'http://cs.58.com/pbdn/pn{}/'.format(i)
        get_one_page(url)
        time.sleep(3)

get_next_page(1,3)



