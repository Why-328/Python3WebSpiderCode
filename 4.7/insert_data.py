from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['https://localhost:9200'], verify_certs=False, http_auth=('elastic', 'TRb3l61J7O73fptWXEcQ'))
es.indices.create(index='news', ignore=400)

data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
}
result = es.create(index='news', id=1, body=data)
print(result)
result = es.index(index='news', body=data) #  _id:VCMVj4gBBBfkyL4kEeQA
print(result)
