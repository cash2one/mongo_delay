from pymongo import MongoClient
import time
task = {"device":
                {'type': "", 'version': '127.22', 'id': ''},
            'guid': 202, 'time': time.time(), 'timeout': 40, 'topic': 'jd_task_kind',
            'interval': 3,  # 任务执行周期间隔时间
            'suspend': 0,  # 暂停标识
            'status': 0,

            'body': {
                'kind': '9987,830,866', 'platform': 'jd_app', 'sort': None,
                "url": "https://list.jd.com/list.html?",
                "maxpage": 0,
                'shopid':1,
                "cookie_type": "jd_web",
                'key_search': 0,
                "data": {
                    'key_word': '',
                    "cat": "670,671,672",
                    "sort": "sort_rank_asc",
                    "trans": "1",
                    "page": "1",
                    "JL": "6_0_0"
                }
            }}



conn = MongoClient('localhost', 27017, connect=False)
db = conn['jame_bd']
tb = db['task_main']
#tb_ready = db['sku_ready_list']
#tb.remove()
#tb_ready.remove()
tb.insert(task)
#tb_ready.insert({'guid':task['guid']})
#a = tb_ready.find_one()



