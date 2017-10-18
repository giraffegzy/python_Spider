from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import time

star = time.clock()
url = 'http://tieba.baidu.com/p/2166231880'
r = requests.get(url)
html = BeautifulSoup(r.text, 'lxml')
url_text = html.find_all("img", {"class": "BDE_Image"})



rzc = r'[a-zA-z]+://[^\s]*'
image = re.compile(rzc)
result = re.findall(image, str(url_text))


i = 0
for get_image in result:
    urllib.request.urlretrieve(get_image, '%s.jpg' % i,)
    i += 1
    print("已经开始下载第%s图片" % i)
print("下载完毕。")
end = time.clock()
print("运行时间:%s 秒" % (end - star))



