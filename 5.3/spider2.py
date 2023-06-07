import pymongo
import requests
import logging
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://dynamic1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies_spa1'
MONGO_COLLECTION_NAME = 'movies_spa1'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies_spa1']
collection = db['movies_spa1']


def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException as e:
        print(e)
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)


def main(page):
    index_data = scrape_index(page)
    for item in index_data.get('results'):
        id = item.get('id')
        detail_data = scrape_detail(id)
        logging.info('detail data %s', detail_data)
        save_data(detail_data)
        logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
