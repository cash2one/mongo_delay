from pymongo import MongoClient
mongo = MongoClient('localhost', 27017, connect=False)
collection = mongo['database']['user']
collection.ensure_index('user_name', unique=True)
try:
    collection.insert({'user_name': 'gddgg1', 'ddd': 111})
except:
    pass
#collection.insert({'user_name':'gddgg1','ddd':111})


collection.ensure_index('user_name', unique=True)
a = collection.find()
for item in a:
    print (item)
