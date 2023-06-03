import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://movie.douban.com/top250'
TOTAL_PAGE = 10
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}


def scrape_page(url):
    """
    爬取页面
    参数为url
    返回值为页面的html
    """
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        logging.error('抓取 %s 时获取了无效状态码 %s', response.status_code, url)
    except requests.RequestException:
        logging.error('抓取 %s 时发生了错误', url, exc_info=True)


def scrape_index(page):
    """
    爬取列表页并且返回列表页html
    参数为页数
    返回列表页的html
    """
    index_url = f'{BASE_URL}?start={(page - 1) * 25}&filter='
    return scrape_page(index_url)


def parse_index(html):
    """
    p解析列表页，得到每一页的详情url
    参数为列表页的html
    """
    doc = pq(html)
    links = doc('.grid_view li .item .info .hd a')
    for link in links.items():
        detail_url = link.attr('href')
        logging.info('详细页面的url为 %s', detail_url)
        yield detail_url


def scrape_detail(url):
    """
    爬取详细信息页面并返回其url，这里不直接调用scrape_page方法是为了以后如果改动也更方便
    参数为详情页的url
    返回值为详情页的html
    """
    return scrape_page(url)


def parse_detail(html):
    """
    解析详情页
    参数为详情页url，例如https://movie.douban.com/subject/1292052/
    返回值data
    """
    doc = pq(html)
    cover = doc('img').attr('src')
    name = doc('h1 > span').text()
    categories = re.findall('<span property="v:genre">(.*?)</span>', str(doc('.clearfix #info span')))
    published_at = re.findall('<span property="v:initialReleaseDate" content=".*?">(.*?)</span>',
                              str(doc('.clearfix #info span')))
    published_at = published_at[0]
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.related-info .indent .all').text() if doc('.related-info .indent .all').text() else doc(
        '.related-info .indent span').text()
    score = doc('.ll.rating_num').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


def save_data(data):
    """
    保存数据到mongodb
    参数为data
    无返回值
    """
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)


def main(page):
    """
    main process
    :return:
    """
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('获取详情页数据 %s', data)
        logging.info('保存数据到 mongodb中............')
        save_data(data)
        logging.info('保存数据成功')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
