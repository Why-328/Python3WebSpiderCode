import pymongo

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

student_list = [
    {
        'id': '20170202',
        'name': 'Mike',
        'age': 21,
        'gender': 'male'
    },
    {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
]

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
result = collection.insert_many(student_list)
print(result)
print(result.inserted_ids)
