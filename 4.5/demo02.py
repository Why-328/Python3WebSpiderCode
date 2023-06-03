import pymongo

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
# 获取students集合的引用
collection = db.students
result = collection.insert_one(student)
print(result)
print(result.inserted_id)
