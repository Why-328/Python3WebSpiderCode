import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
print(client)
client = pymongo.MongoClient('mongodb://localhost:27017/')
print(client)

# 获取test数据库的引用
db = client.test
print(db)
db = client['test']
print(db)
