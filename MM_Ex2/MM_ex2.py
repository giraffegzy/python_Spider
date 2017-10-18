#!user/bin/python
# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
#判断屋主性别
def get_is_man(class_name):
    if class_name == ['member_girl_ico']:
        return "女"
    if class_name == ['member_boy_ico']:
        return "男"
#获取详情页
def get_link(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')

    links = soup.select('#page_list > ul > li > a ')

    for link in links:
        href = link.get("href")
        get_detail_info(href)


#获得详细情况
def get_detail_info(url):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles =soup.select('div.pho_info > h4 > em')
    locations = soup.select('div.pho_info > p > span')
    prices = soup.select('#pricePart > div.day_l > span')
    avtoars = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    images = soup.select('#curBigImage')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')
    for title,location,price,avtoar,image,name,sex in zip(titles,locations,prices,avtoars,images,names,sexs):
        data = {
            "title": title.get_text(),
            "price":price.get_text(),
            "sex": get_is_man(sex.get("class")),
            "name": name.get_text(),
            "avtoar":avtoar.get("src"),
            "image":image.get("src"),
            "location": location.get_text(),
        }
        print(data)

links = ['http://cs.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,11)]

for link in links:
    get_link(link)

