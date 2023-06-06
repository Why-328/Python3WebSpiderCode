# 导入 Elasticsearch 库
from elasticsearch import Elasticsearch

# 创建 Elasticsearch 客户端对象，指定主机地址，验证证书，提供用户名和密码
es = Elasticsearch(hosts=['https://localhost:9200'], verify_certs=False, http_auth=('elastic', 'TRb3l61J7O73fptWXEcQ'))

# 定义要更新的数据
data = {
    'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
    'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
    'date': '2021-07-05'
}

# 定义要更新的文档的索引，文档ID
index = 'news'
doc_id = 1

# 使用 update 方法更新文档，将 data 作为 doc 参数传入
result = es.update(index=index, id=doc_id, body={'doc': data})
# 打印更新结果
print(result)
result = es.index(index=index, id=doc_id, body={'doc': data})
# 打印更新结果
print(result)
