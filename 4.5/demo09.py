import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['students']
results = collection.find({'_id': {'$gt': ObjectId('647aec3f727bc3a86205fdf1')}})
print(results)
for result in results:
    print(result)