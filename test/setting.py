import time


DEVICE_ID = 'jame004'  #设备id
INSTALL_MOUDEL=('pymongo' ,'platform','psutil','multiprocessing','motor','aiohttp','asyncio')#客户端依赖的所有第三方库
UPLOAD_DATA_COUNT = 100#与服务器交互一次上传的最大数据个数
CATCHER_COUNT=1#开启抓取器的进程个数
SUM_PROCESS_COUNT = 4#同时向抓取器填充抓取任务和期望获取解析任务的进程数，这个进程数的大小严重依赖抓取器的效率

AIOHTTP_CONCURRENCY_SUM= 100#抓取器使用aiohttp的并发数


DATABASES = 'jame_bd'  #数据库
DATA_DB = 'data_db'
DATA_TB = 'data_tb'
TASKS_LIST = 'task_main'  #总任务列表


TOPIC = ['jd_task_kind',]#向服务器请求的任务类型

STATUS_DELAY = 0  # 任务处于等待状态
STATUS_READY = 1  # 任务处于就绪状态，可以执行
STATUS_EXCUTING = 2  # 任务正在执行
STATUS_TIMEOUT = 3  # 任务超时
STATUS_DELETED = 4  # 任务处于删除状态，不再被扫描
STATUS_FINISH = 5  # 任务完成，控制权交回队列
ROW_GUID = 'guid'
ROW_TOPIC = 'topic'
ROW_TIME = 'time'
ROW_TIMEOUT = 'timeout'
ROW_BODY = 'body'
ROW_STATUS = 'status'
ROW_INTERVAL = 'interval'
DEVICE_TYPE = 'pc' #设备类型

READY_LIST='_ready_list'#就绪列表的后缀，拼接数据库的后缀

SUM_PROCESS_COUNT = 4#同时向抓取器填充抓取任务和期望获取解析任务的进程数，这个进程数的大小严重依赖抓取器的效率


"""与服务器交互的本地任务相关"""
LOCAL_TASK_TYPE='local_task'#与服务器交互的本地任务类型

"""本地任务所包含的所有任务"""
UPDATE_TASK_LIST = "update_task_list"
UPDATE_MUCH_TASKINFO = "update_much_taskinfo"
UPLOAD_CLIENT_STATUS = "upload_client_status"
UPLOAD_CLIENT_DATA =  "upload_client_data"
UPDATE_PROXY_DATA = "update_proxy_data"
UPDATE_COOKIE_DATA = "update_cookie_data"
REQUEST_SERVER_LIST=(UPDATE_TASK_LIST,UPDATE_MUCH_TASKINFO,UPLOAD_CLIENT_STATUS,
                   UPLOAD_CLIENT_DATA,UPDATE_PROXY_DATA,UPDATE_COOKIE_DATA)


"""本地任务与服务器交互的时间设定"""
UPDATE_TASK_LIST_TIME = 10# 更新任务列表的时间单位是秒
UPDATE_MUCH_TASKINFO_TIME = 5 #客户端回报任务信息的时间,这个时间不应该小于任务的超时时间
UPLOAD_CLIENT_STATUS_TIME = 1*3600 #客户端更新设备信息的时间，1h更新一次
UPLOAD_CLIENT_DATA_TIME = 3 # 客户端回报数据的时间
UPDATE_PROXY_DATA_TIME = 9 #更新proxy的时间
UPDATE_COOKIE_DATA_TIME = 10#更新coolkie 时间
REQUEST_SERVER_TIME = (UPDATE_TASK_LIST_TIME,UPDATE_MUCH_TASKINFO_TIME,UPLOAD_CLIENT_STATUS_TIME,
                       UPLOAD_CLIENT_DATA_TIME,UPDATE_PROXY_DATA_TIME,UPDATE_COOKIE_DATA_TIME)






"""检查客户端与服务器连接情况的任务，断链将重启客户端"""
LOCAL_CHECKTASK_TYPE = 'local_check_task'#检查客户端与服务器的连接情况的任务
LOCAL_CHECK_TASK_TIME = 0.5*3600#以小时为单位





SCRIPT_DIR = 'script_main'#脚本所在的总目录名称



"""服务器地址相关"""
SERVER_IP = '118.187.53.58'
SERVER_PORT = '8989'



def NOW():
    return time.time()


TMP_DB = 'tmp_db'
TMP_TB = 'tmp_tb'