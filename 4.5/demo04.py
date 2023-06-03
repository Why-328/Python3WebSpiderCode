import pymongo
from bson import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['students']
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

result = collection.find_one({'_id': ObjectId('647aef21f3c5f59b1cf9a438')})
print(result)

results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

results = collection.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)

results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
for result in results:
    print(result)
