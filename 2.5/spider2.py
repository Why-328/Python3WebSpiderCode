import json
from os import makedirs
from os.path import exists
import requests
import logging
import re
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')  # 输出格式：时间 - 等级: 信息

BASE_URL = 'https://ssr1.scrape.center'  # 网站地址
TOTAL_PAGE = 10  # 总页数

RESULTS_DIR = 'results'  # 定义保存数据的文件夹
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)  # 判断文件夹是否存在，如果不存在则创建一个


def scrape_page(url):
    """
    爬取页面
    参数为url
    返回值为页面的html
    """
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)  # 访问失败
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)  # 爬取异常


def scrape_index(page):
    """
    爬取列表页并且返回列表页html
    参数为页数
    返回列表页的html
    """
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    """
    解析列表页，得到每一页的详情url
    参数为列表页的html
    """
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')  # 提取超链接href属性
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url
        """
        yield和return类似，在函数中用来返回值给调用者
        使用return的函数是没有状态的，一旦return了，函数就结束了。
        使用yield的函数是有状态的，返回一个值后，还可以继续调用，后面的调用会基于前面的调用状态继续执行，直到所有yield都被用完。
        yield的作用是把一个函数变成生成器(generator)，起到一个延迟的作用。
        """


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
    参数为详情页url，例如https://ssr1.scrape.center/detail/11
    返回值data
    """

    """
    每一部电影的大盒子的class为class="item el-row"，其下面的第一个盒子放的是封面故可以从class="item开始写正则表达式使用非贪婪通用匹配.*?匹配字符至img标签前
    因为要获取电影封面路径因此要使用分组匹配正则表达式(.*?)，因为img标签的class="cover"因此到此结束
    """
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    """
    名称是该页面唯一一个h2标签因此直接匹配h2标签即可，使用分组匹配正则表达式(.*?)获取电影名称
    """
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    """
    电影类别名称包含在span标签中，span标签的外层是button标签，因为button标签不唯一故取其中的class="el-button category el-button--primary el-button--mini"
    做为锁定的条件，使用分组匹配正则表达式(.*?)获取电影类别名称
    """
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    """
    上映时间包含在span标签中，span标签的外层是div标签其中class="m-v-sm info"
    因为其中多了上映两个字所以正则表达式把日期提取出来
    """
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    """
    剧情简介包含在p标签中，外层是class为drama的div标签
    """
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    """
    评分包含在p标签中，外层是class为drama的div标签
    """
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    # .strip返回删除前导和尾随空格的字符串副本。如果给定了chars而不是None，则删除chars中的字符。
    # 电影封面
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    # 电影名称
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    # 电影类型
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    # 上映时间
    published_at = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    # 电影简介
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    # 电影评分
    score = float(re.search(score_pattern, html).group(1).strip()) if re.search(score_pattern, html) else None

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
    将数据存储到json文件
    参数为data
    无返回值
    """
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # ensure_ascii=False保证中文字符在文件中能以正常的中文文本呈现，而不是unicode字符
    # indent=2设置了JSON数据的结果有两格缩进，让JSON数据的格式显得更加美观


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()  # 声明一个进程池
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)  # 第一个参数就是需要被调用的参数，第二个参数就是需要遍历的页码
    pool.close()
