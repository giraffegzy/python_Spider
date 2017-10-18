from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random

client = pymongo.MongoClient('localhost', 27017)
douban = client['douban']
url_list = douban['url_list']
info_list = douban['info_list']
proxies= {'http':'http://XX.XX.XX.XX:XXXX'}

raw_cookie ='gr_user_id=db9ffb51-3d1c-4d25-a922-626a0b40a34f; ll="118371"; bid=Q_RJCHWtdEo; __yadk_uid=rKiJ6Kk84HzxF6NTRklDjRVjt0dRmBOS; viewed="25981277_25862578_27062629_26981446_1200840_26761696"; ps=y; ap=1; ue="271349505@QQ.COM"; dbcl2="168315204:MsgSDEn0tw8"; ck=-2rf; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=cfd853c0-2499-4a04-bf28-27c8f96e7d49; gr_cs1_cfd853c0-2499-4a04-bf28-27c8f96e7d49=user_id%3A1; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1508250204%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%252F%252Fbook.douban.com%252Fsubject%252F25862578%252F%22%5D; _pk_id.100001.3ac3=ea2eb22cc2f6d4d3.1508163097.6.1508250204.1508245350.; _pk_ses.100001.3ac3=*; __utmt_douban=1; __utma=30149280.1540722543.1498134694.1508239235.1508250204.12; __utmb=30149280.1.10.1508250204; __utmc=30149280; __utmz=30149280.1508250204.12.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmv=30149280.16831; __utmt=1; __utma=81379588.1252268416.1508163097.1508239235.1508250204.6; __utmb=81379588.1.10.1508250204; __utmc=81379588; __utmz=81379588.1508250204.6.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _vwo_uuid_v2=A121CE893361136B437CBA31035AA065|d8e3bc344e5094ba88d214231d3f7928; push_noty_num=0; push_doumail_num=0'
cookies = {}
for line in raw_cookie.split(';'):
    key,value = line.split('=',1)
    cookies[key]=value
def get_all_links(url):
        wb_data = requests.get(url,cookies=cookies)
        time.sleep(2)
        soup = BeautifulSoup(wb_data.text,'lxml')
        links = soup.select(' ul > li > div.info > h2 > a')

        if soup.find('li','subject-item'):
                for link in links:
                    url = link.get('href')
                    url_list.insert_one({'url':url})
                    print(url)
        else:
            pass
def start_links():
    for page in range(0,1000,20):
       url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(page)
       get_all_links(url)



def get_detail(url):
    wb_data = requests.get(url,cookies=cookies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(4)
    titles = soup.select(' h1 > span')
    authors = soup.select('#info > a')
    scores = soup.select('#interest_sectl > div > div.rating_self.clearfix > strong')
    marks = soup.select('#interest_sectl > div > div.rating_self.clearfix > div > div.rating_sum > span > a')


    for title,author,score,mark in zip(titles,authors,scores,marks):
        data = {
            "title":title.get_text(),
            "author":author.get_text().strip().split(),
            "score":score.get_text(),
            "mark":mark.get_text()
        }
        print(data)
        info_list.insert_one(data)

get_detail('https://book.douban.com/subject/25862578/')