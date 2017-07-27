from pymongo import  MongoClient
from gridfs import *
from bson import ObjectId

conn = MongoClient('localhost', 27017)
db = conn['tmp_db']
fs = GridFS(db, 'body')  # 存储任务body的大文档，无空间限制

def choice_table(tb):
    return db[tb]

tb = choice_table('jd_task_kind')
data = tb.find_one()
obj_id = data['body']  # 得到存储数据的id
body = fs.get(ObjectId(obj_id)).read()# 从文档中读出body字段{'result':'',data:''}
body = eval(body)  # 还原body
data['result'] = body['result']
data['data'] = body['data']
print (data['data'])