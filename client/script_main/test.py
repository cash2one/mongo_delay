from pymongo import MongoClient
import copy
conn = MongoClient('localhost', 27017, connect=False)
db = conn['test1']
tb = db['test1']
b = tb.find().limit(-100)
a  = copy.copy(b)
for i in b:
    print (i)

print ('jjj')

for i in a:
    print (i)