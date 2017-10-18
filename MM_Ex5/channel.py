from bs4 import BeautifulSoup
import requests

def Top_book():
    url_list = ['https://book.douban.com/chart?subcat=F', 'https://book.douban.com/chart?subcat=I']
    for url in url_list:
        wb_data = requests.get(url)

        soup = BeautifulSoup(wb_data.text,'lxml')

        titles = soup.select(' ul > li > div.media__body > h2 > a')
        authors = soup.select(' ul > li > div.media__body > p.subject-abstract.color-gray')
        marks = soup.select(' ul > li > div.media__body > p.clearfix.w250 > span.fleft.ml8.color-gray')

        for title,author,mark in zip(titles,authors,marks):
            data = {
                "title":title.get_text(),
                "author":author.get_text().strip().split()[0]+author.get_text().strip().split()[1],
                "mark":mark.get_text(),
                "price":author.get_text().strip().split('/')[3]
            }
            print(data)


def get_tags_link():
    url = 'https://book.douban.com/'
    host_url = 'https://book.douban.com'

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    tags_links = soup.select(' ul > li > ul > li > a')

    for tag in tags_links:
        tag_link = host_url + tag.get('href')
        print(str(tag_link))

Top_book()
channel = '''
https://book.douban.com/tag/小说
https://book.douban.com/tag/随笔
https://book.douban.com/tag/日本文学
https://book.douban.com/tag/散文
https://book.douban.com/tag/诗歌
https://book.douban.com/tag/童话
https://book.douban.com/tag/名著
https://book.douban.com/tag/港台
https://book.douban.com/tag/漫画
https://book.douban.com/tag/推理
https://book.douban.com/tag/绘本
https://book.douban.com/tag/青春
https://book.douban.com/tag/科幻
https://book.douban.com/tag/言情
https://book.douban.com/tag/武侠
https://book.douban.com/tag/奇幻
https://book.douban.com/tag/历史
https://book.douban.com/tag/哲学
https://book.douban.com/tag/传记
https://book.douban.com/tag/设计
https://book.douban.com/tag/建筑
https://book.douban.com/tag/电影
https://book.douban.com/tag/回忆录
https://book.douban.com/tag/音乐
https://book.douban.com/tag/旅行
https://book.douban.com/tag/励志
https://book.douban.com/tag/职场
https://book.douban.com/tag/教育
https://book.douban.com/tag/美食
https://book.douban.com/tag/灵修
https://book.douban.com/tag/健康
https://book.douban.com/tag/家居
https://book.douban.com/tag/经济学
https://book.douban.com/tag/管理
https://book.douban.com/tag/商业
https://book.douban.com/tag/金融
https://book.douban.com/tag/营销
https://book.douban.com/tag/理财
https://book.douban.com/tag/股票
https://book.douban.com/tag/企业史
https://book.douban.com/tag/科普
https://book.douban.com/tag/互联网
https://book.douban.com/tag/编程
https://book.douban.com/tag/交互设计
https://book.douban.com/tag/算法
https://book.douban.com/tag/通信
https://book.douban.com/tag/神经网络
'''
