from page_parsing import get_detail,url_list
import pymongo
from multiprocessing import Pool

def get_all_link():
    for link in url_list.find():
        url = link['url']

        yield url
if __name__ == '__main__':
    pool = Pool()
    pool.map(get_detail,[link for link in get_all_link()])

