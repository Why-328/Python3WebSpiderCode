import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test']
collection = db['students']
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {"$set": student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
