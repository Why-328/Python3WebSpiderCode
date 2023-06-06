from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['https://localhost:9200'], verify_certs=False, http_auth=('elastic', 'TRb3l61J7O73fptWXEcQ'))
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
es.indices.put_mapping(index='news', body=mapping)
