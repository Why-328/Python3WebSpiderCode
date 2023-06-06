# 导入 Elasticsearch 库
from elasticsearch import Elasticsearch

# 创建 Elasticsearch 客户端对象，指定主机地址，验证证书，提供用户名和密码
es = Elasticsearch(hosts=['https://localhost:9200'], verify_certs=False, http_auth=('elastic', 'TRb3l61J7O73fptWXEcQ'))

# 定义要创建的索引的名称
index = 'news'

# 使用 create 方法创建索引
result = es.indices.create(index=index)

# 打印创建结果
print(result)
