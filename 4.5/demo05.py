import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test
collection = db.students

count = collection.count_documents()
print(f"查询结果包含{count}条数据")

query = {"age": 20}
count = collection.count_documents(query)
print(f"查询结果包含{count}条数据")
