from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['https://localhost:9200'], verify_certs=False, http_auth=('elastic', 'TRb3l61J7O73fptWXEcQ'))
result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
