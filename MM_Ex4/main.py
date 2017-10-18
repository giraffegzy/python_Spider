from multiprocessing import Pool
from ex4_channel import channel_list
from ex4_page_parsing import get_links_from,get_detail_info,url_list

def get_all_links_from(channel):
    for num in range(1, 101):
        get_links_from(channel,num)


def get_link_getone():
    for info in url_list.find():
        if 'jump' in info["url"]:
            print("1")
        else:
            url = info["url"]
            yield url

if __name__ == "__main__":
     #pool = Pool()
     #pool.map(get_all_links_from,channel_list.split())
     pool2 = Pool()
     pool2.map(get_detail_info,[link for link in get_link_getone()])

