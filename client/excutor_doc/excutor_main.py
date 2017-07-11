
#此脚本将从中间层获取任务，执行器，抓取器，解析器，发送器的功能方法都封装,本地一个任务封装了一组相同类型的任务
#可进行业务拆分

"""
topic名称定义：
抓取任务：jm_crawl
解析任务：parsing
发送任务：send

"""

import time,sys
from client_doc import setting
from excutor_doc import db_oprate

class excutor_cls:
    def __init__(self):
        self.count = 0
        #lib requests/aiohttp
        #本地生成的任务格式统一如下，服务器生成的多个本地任务将全部集成到一个任务中
        self.local_task = {

                            'topic':'jm_crawl',
                             'guid':'',#沿用服务器下发的任务id
                             'body':
                                    {
                                     'crawl':{'name':'','version':''},
                                     'urls':'',
                                     'abstime':'',
                                    #异步字段（是否使用异步）
                                    #使用平台
                                    #content主要是一组任务共有的关键信息
                                     'content':{

                                                'proxymode':'auto','encode':'utf-8',
                                                'lib':'aiohttp','max_retry':0,'bulk':False,
                                                'cookie':'','debug':False,'usephantomjs':False,

                                               },
                                    'result':[],#{'url': '', 'time': '', 'html': '', 'error': '', 'proxy': '', 'retry': 0, 'headers': '', 'other': '', 'sucess': False, 'platform': ''}
                                    'parsing_data':[],
                                    'callback':{"topic":'parsing',},
                                    }

                             }#excutor_interface的输出，catcher_interface的输入

        self.db_obj = db_oprate.collection_db()  # 操作数据库对象


    def yield_get_interface(self):
        tb = self.db_obj.choice_crawl_table()  # 进入抓取任务表
        next_topic = yield
        try:
            task = self.db_obj.find_modify_remove(tb, {'topic': next_topic})
            # 获取解析任务并从数据表中删除
        except Exception as e:
            print('insert db error!!!!', e)
        if task:
            obj_id = task['body']
            body = self.db_obj.gridfs_get_crawldata(obj_id)  # 读出gridfs
            self.db_obj.gridfs_del_crawldata(obj_id)  # 将body从文档中删除
            body = eval(body)  # 还原body
            task['body'] = body
            yield task
        else:
            yield None

    def yield_send_interface(self):
        #外部使用实例
        """
        f = yield_interface()
        f.send(None)
        f.send(task)#将任务发送到函数中，返回值为'insert crawl_task'
        到了预定时间，希望得到结果
        f.send(None)#如果有解析任务就返回任务，没有的话就返回None
        """
        print('input interface****************')
        dict = yield #发送的任务
        next_topic = "".join([str(dict['topic']), str(dict['guid'])])  # 通过服务器下发任务的guid和topic拼接需要获取的任务类型
        # 根据时间戳生成随机的uuid + guid 拼接成新的任务类型，同一时间线程同时运行，可能产生重复的值
        task = {'topic': 'JM_Crawl',
                'guid': dict['guid'],  # 沿用服务器下发的任务id
                'body':
                    {
                        'crawl': {'name': '', 'version': '1.1.1.1'},
                        'urls': dict['urls'],
                        'abstime': str(time.time()),
                        # content主要是一组任务共有的关键信息
                        'content': {

                            'proxymode': 'auto', 'encode': 'utf-8',
                            'lib': 'aiohttp', 'max_retry': 0, 'bulk': False,
                            'cookie': '', 'debug': False, 'usephantomjs': False,

                        },
                        'callback': {'topic': next_topic, 'guid': dict['guid']},
                        'result': [],
                        # {'url': '', 'time': '', 'html': '', 'error': '', 'proxy': '', 'retry': 0, 'headers': '', 'other': '', 'sucess': False, 'platform': ''}
                        'parsing_data': [],
                    }
                }

        # 将抓取任务插入数据库
        tb = self.db_obj.choice_crawl_table()  # 进入抓取任务表
        self.db_obj.insert_data(tb, task)  # 将抓取任务添加到数据库中
        m = yield next_topic#

    def send_interface(self,task):#返回值为下次任务的类型
        f = self.yield_send_interface()#生成函数迭代器
        f.send(None)
        next_topic= f.send(task)#生成抓取任务,并且返回结果类型
        return next_topic
    def get_interface(self,next_topic,timeout):#参数一：获取任务的类型。参数二：超时时间
        start_time = time.time()
        while True:
            f = self.yield_get_interface()  # 生成函数迭代器
            f.send(None)
            task = f.send(next_topic)#得到结果返回结果，没有结果返回None
            if task:
                return task
            if time.time()-start_time >= timeout:#获取任务超时
                return task
            else:
                time.sleep(0.1)#没有超时，也没得到任务休眠1s

    def yield_interface(self,task,timeout):
        next_topic = self.send_interface(task)#生成抓取任务，返回下次得到任务的类型
        task = self.get_interface(next_topic,timeout)#得到结果，超时时间内得不到数据返回None
        return task


    def interface(self, dict):  # 参数必须是一个字典
        print ('input interface****************')
        next_topic = "".join([str(dict['topic']),str(dict['guid'])])#通过服务器下发任务的guid和topic拼接需要获取的任务类型
        # 根据时间戳生成随机的uuid + guid 拼接成新的任务类型，同一时间线程同时运行，可能产生重复的值
        task = {'topic': 'JM_Crawl',
                'guid': dict['guid'],  # 沿用服务器下发的任务id
                'body':
                    {
                        'crawl': {'name': '', 'version': '1.1.1.1'},
                        'urls': dict['urls'],
                        'abstime': str(time.time()),
                        # content主要是一组任务共有的关键信息
                        'content': {

                            'proxymode': 'auto', 'encode': 'utf-8',
                            'lib': 'aiohttp', 'max_retry': 0, 'bulk': False,
                            'cookie': '', 'debug': False, 'usephantomjs': False,

                        },
                        'callback': {'topic': next_topic,'guid':dict['guid']},
                        #'result': [],
                        # {'url': '', 'time': '', 'html': '', 'error': '', 'proxy': '', 'retry': 0, 'headers': '', 'other': '', 'sucess': False, 'platform': ''}
                        'parsing_data': [],
                    }
                }

        #将抓取任务插入数据库
        tb = self.db_obj.choice_crawl_table()#进入抓取任务表
        self.db_obj.insert_data(tb,task)#将抓取任务添加到数据库中
        while True:
            #查表
            try:
                task = self.db_obj.find_modify_remove(tb,{'topic':next_topic})
                # 获取解析任务并从数据表中删除
            except Exception as e:
                print('insert db error!!!!', e)
            if task:
                obj_id = task['body']
                body = self.db_obj.gridfs_get_crawldata(obj_id)#读出gridfs
                self.db_obj.gridfs_del_crawldata(obj_id)  # 将body从文档中删除
                body = eval(body)  # 还原body
                task['body'] = body
                return task
            else:
                time.sleep(0.1)



    """存储到上传数据库的数据接口"""
    def data_save(self,mes):#保存数据接口，大于16M的数据接口
        grif = {'result': '', 'data': ''}
        try:
            """得到的抓取数据中的result,data字段存放在gridfs中"""
            grif['result'] = mes['result']  # 抓取的url必要信息
            grif['data'] = mes['data']  # 解析数据的必要信息
            obj_id =self.db_obj.gridfs_put_data(grif)
            mes.pop('result')
            mes.pop('data')
            mes['data_lenth_flag'] = 1#数据大于16m标识
            mes['upload_type'] = 'data'#上传的数据类型为数据
            mes['body'] = str(obj_id)  # 将文档的id存储到body中
            tb = self.db_obj.choice_data_table()#进去上传数据表
            self.db_obj.insert_data(tb,mes)
            # 只将解析结果添加到数据库

        except Exception as e:
            print('保存上传数据的数据库失败：', e)
        # 将任务的状态进行更改,根据类型判断更改状态的值
        if 1 == 1:  # 周期性任务
            table = self.db_obj.choice_task_table()  # 进入任务表
            self.db_obj.find_modify(table, {setting.ROW_GUID: mes[setting.ROW_GUID]},
                                    {'$set': {setting.ROW_STATUS: setting.STATUS_FINISH}})

        else:  # 一次性任务
            table = self.db_obj.choice_task_table()  # 进入任务表
            self.db_obj.find_modify(table, {setting.ROW_GUID: mes[setting.ROW_GUID]},
                                    {'$set': {setting.ROW_STATUS: setting.STATUS_DELETED}})
            # 一次行任务同样是周期性任务，扫描任务负责删除

    def data_lt16M_save(self,mes):#存储小于16M的数据接口
        mes['data_lenth_flag'] = 0  # 数据小于16m标识
        mes['upload_type'] = 'data'  # 上传的数据类型为数据
        tb = self.db_obj.choice_data_table()  # 进去上传数据表
        self.db_obj.insert_data(tb, mes)
        if 1 == 1:  # 周期性任务
            table = self.db_obj.choice_task_table()#进入任务表
            self.db_obj.find_modify(table,{setting.ROW_GUID: mes[setting.ROW_GUID]},{'$set': {setting.ROW_STATUS: setting.STATUS_FINISH}})

        else:  # 一次性任务
            table = self.db_obj.choice_task_table()  # 进入任务表
            self.db_obj.find_modify(table, {setting.ROW_GUID: mes[setting.ROW_GUID]},
                                    {'$set': {setting.ROW_STATUS: setting.STATUS_DELETED}})
            # 一次行任务同样是周期性任务，扫描任务负责删除

    def html_save(self,mes):#存储未得到解析的html文件接口
        mes['data_lenth_flag'] = 0  # 数据小于16m标识
        mes['upload_type'] = 'html'  # 上传的数据类型为无法得到解析的html
        tb = self.db_obj.choice_data_table()  # 进去上传数据表
        self.db_obj.insert_data(tb, mes)



    def split_upload_data(self,mes):#拆分数据
        data_size = sys.getsizeof(mes)#得到数据大小，单位是字节
        pass



if __name__ =='__main__':


    #task = t.Access_to_task('get_task','',count=1)[0]
    #print (task)
    #t.catcher_interface(task)#抓取任务接口，因为本地任务是相同类型任务的集合，所以此接口内部一次只取一个任务，然后分解并发
    #t.parsing_interface(task)

    """
    for i in task_list:
        t.excutor_interface(i)
    """