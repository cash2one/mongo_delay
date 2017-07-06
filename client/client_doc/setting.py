import time

"""服务器地址相关"""
SERVER_IP = 'localhost'
SERVER_PORT = '5500'
DEVICE_TYPE = 'pc' #设备类型
DEVICE_ID = 'jame000'  #设备id

INSTALL_MOUDEL=('pymongo' ,'platform','psutil','multiprocessing','motor','aiohttp','asyncio')#客户端依赖的所有第三方库

CATCHER_COUNT=1#开启抓取器的进程个数
SUM_PROCESS_COUNT = 4#同时向抓取器填充抓取任务和期望获取解析任务的进程数，这个进程数的大小严重依赖抓取器的效率
AIOHTTP_CONCURRENCY_SUM= 100#抓取器使用aiohttp的并发数


##############################"""与服务器交互的本地任务相关"""####################################################

CONNECT_SERVER_TYPE = ('zmq','http')#选择与服务器通信方式,http更加稳定，列表的元素
LOCAL_TASK_TYPE=CONNECT_SERVER_TYPE[1]+'_local_task'#与服务器交互的本地任务类型，客户端与服务器端的通信必须保持一致

##############################"""与服务器交互的本地任务相关"""###################################################


#########################"""数据库相关"""####################################################


DATABASES = 'jame_bd'  #数据库
TASKS_LIST = 'task_main'  #总任务列表


DATA_DB = 'data_db'#存储上传数据的数据库
DATA_TB = 'data_tb'#存储上传数据的表
UPLOAD_DATA_BODY = 'body'#存储上传数据的body,由于上传数据可能大于16M，所以采用gridfs


CRAWL_TASK_DATA = 'pasrsing_data'#存储抓取任务的数据库
CRAWL_TASK_TABLE = 'pasrsing_tb'#存储抓取任务的数据表，interface将抓取任务插入该数据表，抓取器从该表中获取任务并删除
CRAWL_TASK_BODY  = 'test'#存储抓取任务抓取到的数据拼接成的解析任务的body部分，对应的mongo  gridfs的存储大于16M的数据，主要起到一个中转的作用

#########################"""数据库相关"""####################################################

TOPIC = ['jd_task_kind','jm_task_proxycrawl']#向服务器请求的任务类型

##############################"""任务字段，与任务状态"""############################################
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

##############################"""任务字段，与任务状态"""############################################



READY_LIST='_ready_list'#就绪列表的后缀，拼接数据库的后缀"_ready_list"



##############################"""本地任务相关（主要是与服务器交互）"""############################################

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


#特殊的本地任务，该本地任务只在选择与服务器交互使用zmq时生效，该任务主要是因为zmq rep req通信时存在断连无法重连的情况增加的检查机制
"""检查客户端与服务器连接情况的任务，断链将重启客户端"""
LOCAL_CHECKTASK_TYPE = 'local_check_task'#检查客户端与服务器的连接情况的任务
LOCAL_CHECK_TASK_TIME = 0.5*3600#以小时为单位


##############################"""本地任务相关（主要是与服务器交互）"""############################################




SCRIPT_DIR = 'script_main'#脚本所在的总目录名称



def NOW():
    return time.time()