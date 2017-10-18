#!user/bin/python
# -*-coding:utf-8 -*-
#异步加载
from bs4 import BeautifulSoup
import requests
import time
url = 'https://knewone.com/discover?page='

def get_pages(url,data=None):
    wb_data =requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select(' section.content > h4 > a')
    images = soup.select('a.cover-inner > img')
    links =soup.select('section.content > h4 > a')
    if data ==None:
        for title,image,link in zip(titles,images,links):
            data = {
                "title":title.get_text(),
                "image":image.get("src"),
                "link":link.get("href")
            }
            print(data)

def get_more_pages(start,end):
    for i in range(start,end):
        get_pages(url+str(i))
        time.sleep(2.5)


get_more_pages(1,15)