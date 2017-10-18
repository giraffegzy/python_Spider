from bs4 import BeautifulSoup
import requests
import pymongo

start_url = 'http://xa.58.com/sale.shtml'
url_host = 'http://xa.58.com'
def get_channel_url(url):
    wb_data =requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

channel_list = '''
http://xa.58.com/tongxunyw/
http://xa.58.com/danche/
http://xa.58.com/diandongche/
http://xa.58.com/fzixingche/
http://xa.58.com/sanlunche/
http://xa.58.com/peijianzhuangbei/
http://xa.58.com/diannao/
http://xa.58.com/bijiben/
http://xa.58.com/pbdn/
http://xa.58.com/diannaopeijian/
http://xa.58.com/zhoubianshebei/
http://xa.58.com/shuma/
http://xa.58.com/shumaxiangji/
http://xa.58.com/mpsanmpsi/
http://xa.58.com/youxiji/
http://xa.58.com/ershoukongtiao/
http://xa.58.com/dianshiji/
http://xa.58.com/xiyiji/
http://xa.58.com/bingxiang/
http://xa.58.com/jiadian/
http://xa.58.com/binggui/
http://xa.58.com/chuang/
http://xa.58.com/ershoujiaju/
http://xa.58.com/yingyou/
http://xa.58.com/yingeryongpin/
http://xa.58.com/muyingweiyang/
http://xa.58.com/muyingtongchuang/
http://xa.58.com/yunfuyongpin/
http://xa.58.com/fushi/
http://xa.58.com/nanzhuang/
http://xa.58.com/fsxiemao/
http://xa.58.com/xiangbao/
http://xa.58.com/meirong/
http://xa.58.com/yishu/
http://xa.58.com/shufahuihua/
http://xa.58.com/zhubaoshipin/
http://xa.58.com/yuqi/
http://xa.58.com/tushu/
http://xa.58.com/tushubook/
http://xa.58.com/wenti/
http://xa.58.com/yundongfushi/
http://xa.58.com/jianshenqixie/
http://xa.58.com/huju/
http://xa.58.com/qiulei/
http://xa.58.com/yueqi/
http://xa.58.com/bangongshebei/
http://xa.58.com/diannaohaocai/
http://xa.58.com/bangongjiaju/
http://xa.58.com/ershoushebei/
http://xa.58.com/chengren/
http://xa.58.com/nvyongpin/
http://xa.58.com/qinglvqingqu/
http://xa.58.com/qingquneiyi/
http://xa.58.com/chengren/
http://xa.58.com/xiaoyuan/
http://xa.58.com/ershouqiugou/
http://xa.58.com/tiaozao/
'''


