#-*- utf-8 -*-
import uuid,time,requests,pymongo
from excutor_doc.jd_tools import *
from excutor_doc.excutor_main import *

from pymongo import MongoClient
class jm_task_proxyverificate:

    @classmethod
    def updateDict(cls, args):
        basic_task = {'device': {'type': '', 'version': '127.22', 'id': ''},
                      'guid': args['guid'],
                      'time': args['time'],  # time.time(),
                      'timeout': 1200,
                      'topic': 'jm_task_proxyverificate',
                      'interval': 86400,  # 任务执行周期间隔时间
                      'suspend': 0,  # 暂停标识
                      'status': 0,
                      'body': args['body']
                      }
        return basic_task
    @classmethod
    def getVerificateTask(cls):
        # 检查数据库,将大于验证时间的代理挑出来
        proxylist = [{"ip":"120.210.32.5","port":"80","ptl":"https","score":{"www_baidu_com":
                                                                                        {"responseTime":32,
                                                                                         "transfersVelocity":3,
                                                                                         "lastTime":"2017-06-09 11:02:30 GMT",
                                                                                         "score":10,
                                                                                         "usecount":100,
                                                                                         "suscesscount":50,
                                                                                         "useInterval":502
                                                                                        },
                                                                            "www_jd_com":{"responseTime":32,
                                                                                         "transfersVelocity":3,
                                                                                         "lastTime":"2017-06-09 11:02:30 GMT",
                                                                                         "score":10,
                                                                                         "usecount":100,
                                                                                         "suscesscount":50,
                                                                                         "useInterval":502
                                                                                        },
                                                                            "www_taobao_com":
                                                                                        {"responseTime":32,
                                                                                         "transfersVelocity":3,
                                                                                         "lastTime":"2017-06-09 11:02:30 GMT",
                                                                                         "score":10,
                                                                                         "usecount":100,
                                                                                         "suscesscount":50,
                                                                                         "useInterval":502
                                                                                        },
                                                                            "www_google_com":
                                                                                       {"responseTime":32,
                                                                                         "transfersVelocity":3,
                                                                                         "lastTime":"2017-06-09 11:02:30 GMT",
                                                                                         "score":10,
                                                                                         "usecount":100,
                                                                                         "suscesscount":50,
                                                                                         "useInterval":502
                                                                                        }},
                      "task": {"verificate": {"www_baidu_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_jd_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_taobao_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_google_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   }
                                              }}},
                     {"ip": "188.25.25.5", "port": "80", "ptl": "https", "score": {"www_baidu_com":
                                                                                        {"responseTime": 32,
                                                                                         "transfersVelocity": 3,
                                                                                         "lastTime": "2017-06-09 11:02:30 GMT",
                                                                                         "score": 10,
                                                                                         "usecount": 100,
                                                                                         "suscesscount": 50,
                                                                                         "useInterval": 502
                                                                                         },
                                                                                    "www_jd_com": {"responseTime": 32,
                                                                                                   "transfersVelocity": 3,
                                                                                                   "lastTime": "2017-06-09 11:02:30 GMT",
                                                                                                   "score": 10,
                                                                                                   "usecount": 100,
                                                                                                   "suscesscount": 50,
                                                                                                   "useInterval": 502
                                                                                                   },
                                                                                    "www_taobao_com":
                                                                                        {"responseTime": 32,
                                                                                         "transfersVelocity": 3,
                                                                                         "lastTime": "2017-06-09 11:02:30 GMT",
                                                                                         "score": 10,
                                                                                         "usecount": 100,
                                                                                         "suscesscount": 50,
                                                                                         "useInterval": 502
                                                                                         },
                                                                                    "www_google_com":
                                                                                        {"responseTime": 32,
                                                                                         "transfersVelocity": 3,
                                                                                         "lastTime": "2017-06-09 11:02:30 GMT",
                                                                                         "score": 10,
                                                                                         "usecount": 100,
                                                                                         "suscesscount": 50,
                                                                                         "useInterval": 502
                                                                                         }},
                      "task": {"verificate": {"www_baidu_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_jd_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_taobao_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   },
                                              "www_google_com":
                                                  {"interval": 86400,
                                                   "lastTime": "2017-06-09 09:03:30 GMT",
                                                   "status": 0,
                                                   "timeout": 300
                                                   }
                                              }}
                      }]
        return proxylist

    @classmethod
    def generatepvtask(cls,ptb):
        proxyiplist=[]
        arr = ptb.find({'ipInfo.status':2})
        for item in arr:
            item.pop('_id')
            proxyiplist.append(item)
        return proxyiplist
    @classmethod
    def generateTask(cls):
        conn = MongoClient('localhost', 27017)
        pdb = conn['jame_bd']
        ptb = pdb['jame_proxy']
        tasktb = pdb['task_main']
        proxylist = cls.generatepvtask(ptb)#cls.getVerificateTask()
        tasks = []
        count = 0
        addN = 0#3
        for i in range(len(proxylist)):
            guid = str(uuid.uuid1())  # 根据时间戳生成随机的uuid
            dictUpdate = {'guid': guid, 'time': time.time() + count,
                          'body': proxylist[i]}
            basic_task = cls.updateDict(dictUpdate)
            tasktb.insert(basic_task)
            tasks.append(basic_task)
            count += addN
        return tasks

    @classmethod
    def getHostlist(cls,task):
        hostlist=[]
        hostDict = task['body']['ipInfo']['task']['verifi']
        for index,item in enumerate(hostDict):
            host = item.replace('__','/').replace('_','.')
            hostlist.append(host)
        return hostlist

    @classmethod
    def get_urls(cls, task, obj):
        print ("proxyverificateTask:",task)
        ip = task['body']['ipInfo']['ip']
        port = task['body']['ipInfo']['port']
        ptl = task['body']['ipInfo']['ptl']
        urlList = []
        page = 1
        hostlist=cls.getHostlist(task)
        method = 'GET'
        myheader = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, sdch',
            'accept-language': 'zh-CN,zh;q=0.8',
            'connection': 'keep-alive',
            #   'origin': '',
            #     'host': '',
       #     'referer': '',
            'user-agent': '',
            #   'cookie': ''
        }
      #  myheader['referer'] = 'http://baidu.com/'
      #  myheader['host']='www.baidu.com'
      #  myheader['host']='www.taobao.com'
        myheader['user-agent'] = jd_tools.get_web_useragent()
        useproxy = True
        proxy = {'ip':ip,'port':port,'ptl':ptl}
        for i in range(len(hostlist)):
            url = 'http://'+hostlist[i]
            myurl = {'url': url, 'method': method, 'header': myheader, 'useproxy': useproxy,'proxy':proxy}
            urlList.append(myurl)
            url = 'https://' + hostlist[i]
            myurl = {'url': url, 'method': method, 'header': myheader, 'useproxy': useproxy, 'proxy': proxy}
            urlList.append(myurl)
        return urlList

    @classmethod
    def parser(cls, html, task):
      #  print ("验证任务的解析:",task)
        data = False
        if task.get('url').get('url')=='http://www.baidu.com' or 'https://www.baidu.com':
            if html.find("百度一下，你就知道") != -1:
                data = True
        elif task.get('url').get('url')=='http://www.jd.com' or 'https://www.jd.com':
            if html.find("淘宝网")!=-1:
                data = True
        elif task.get('url').get('url')=='http://www.taobao.com' or 'https://www.taobao.com':
            if html.find("京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")!=-1:
                data=True
        return data

    @classmethod
    def isAntiSpider(cls, html, task):
        return False

    @classmethod
    def score(cls,proxy):
        score = 0
        return score

    @classmethod
    def run(cls,task,obj_db):#dbcon 数据库连接
        print("proxyverificaterun+++++++++++++")
        obj = excutor_cls(obj_db)
        urls = cls.get_urls(task, obj)
        arg = {'urls': urls, 'guid': task['guid'], 'topic': task['topic']}
        #---------------------------------------------------------------抓取器
        next_topic = "".join([str(arg['topic']), str(arg['guid'])])
        ptask = {
            'topic': next_topic,
            'guid': arg['guid'],  # 沿用服务器下发的任务id
            'body': {'crawl': {'name': '', 'version': ''},
                     'urls': arg['urls'],
                     'abstime': '',
                     # content主要是一组任务共有的关键信息
                     'content': {'proxymode': 'auto', 'encode': 'utf-8', 'lib': 'requests', 'max_retry': 0,
                                 'bulk': False, 'cookie': '', 'debug': False, 'usephantomjs': False, },
                     'result': [],
                     # {'url': '', 'time': '', 'html': '', 'error': '', 'proxy': '', 'retry': 0, 'headers': '', 'other': '', 'sucess': False, 'platform': ‘’,’guid’:,’’(服务器下发的guid),’task_count’:urls字段的元素数,’callback’:{'topic’:next_topic,’guid':dict['guid’]},#callback里的’guid’是系统下发任务时的guid,next_topic为以时间戳产生的uuid码}
                     'parsing_data': [],
                     'callback': {"topic": 'parsing', },
                     }
        }
        for index, item in enumerate(arg.get('urls')):  # [{'url': url, 'useproxy': True, 'header': self.get_header(),'host':host} for url in urls]#'method': 'GET',
            tempitem = {}
            tempitem['url'] = item
            method = item.get('method', 'GET')
            url = item.get('url')
            header = item.get('header')
            useproxy = item.get('useproxy')
            data = None
            proxy = None
            proxyip = None
            if item.get('url') and item.get('useproxy') == True:
                if item.get('proxy'):
                    proxy = item.get('proxy')

            if proxy and (len(proxy.get('ip')) < 7):
                continue

            if proxy:
                if isinstance(proxy.get('ip'), bytes):
                    proxy = proxy.get('ip').decode('utf-8')
                real_proxy = {'http': 'http://' + proxy.get('ip') + ':' + str(proxy.get('port')),
                              'https': 'http://' + proxy.get('ip') + ':' + str(proxy.get('port'))}
            data = item.get('data')
            tempitem['retry'] = 0
            tempitem['sucess'] = False
            tempitem['html'] = ''
            html = None
            for i in range(5):
                try:
                    if method == 'POST':
                        resp = requests.post(url, data=data, headers=header, proxies=real_proxy, timeout=20)  #
                        if resp.status_code == 200:
                            html = resp.text
                    elif method == 'GET':
                        resp = requests.get(url, params=data, headers=header, proxies=real_proxy, timeout=20)  #
                        if resp.status_code == 200:
                            html = resp.text
                except Exception as e:
                    print('Get error:', e)
                finally:
                    if tempitem['retry'] >= 1:
                        if (proxyip is None) and item.get('useproxy') == True:
                            break
                     #   proxyip = self.getdefaultproxy(obj)
                      #  if proxyip:
                      #      proxy = proxyip.get('ipInfo')
                      #      print('is changing proxy ', proxy.get('ip'), ':', proxy.get('port'), ',', proxy.get('ptl'))
                    if html:
                        tempitem['sucess'] = True
                        tempitem['html'] = html
                        break
                    else:
                        if tempitem['retry'] >= 5:
                            break
                        tempitem['retry'] += 1
            ptask['body']['result'].append(tempitem)
        #----------------------------------------------------------
        #ptask = obj.interface(arg)
        # print (ptask,"*************ptask")
        zresult = {'guid': task['guid'], 'status': 0, 'result': [], 'data': []}
        passok=False
        if ptask:
            results = ptask['body']['result']#[0]
            for index, _result in enumerate(results):
                print("proxyverificateloop++++", index)
                if cls.isAntiSpider(_result['html'], _result):
                    zresult['result'].append({'host': _result['url']['url'], 'proxy':_result['url']['proxy'],
                                              'html': 'isAntiSpider'})
                    continue
                data = cls.parser(_result['html'], _result)
                if data:
                    zresult['result'].append({'host': _result['url']['url'],'proxy':_result['url']['proxy'],
                                              'html': 'has parsed'})
                    passok=True
                else:
                    zresult['result'].append({'host': _result['url']['url'],'proxy':_result['url']['proxy'],
                                              'html': 'error'})#_result['html']

            zresult['topic'] = task.get('topic')
            zresult['data'] = task.get('body').get('ipInfo')
            obj.data_save(zresult)
            if passok == True: # .append({'isok':data,'proxy':_result['url']['proxy']})
                try:
                    ptb = obj.db_obj.choice_table('jame_proxy')
                    pindex = list(ptb.index_information())
                    if 'ipInfo.ip_1_ipInfo.port_1_ipInfo.ptl_1' not in pindex:
                        ptb.create_index([('ipInfo.ip', pymongo.ASCENDING), ('ipInfo.port', pymongo.ASCENDING),('ipInfo.ptl', pymongo.ASCENDING)], unique=True)
                    tempdata= task.get('body')
                    tempdata['ipInfo']['status']=1
                    obj.db_obj.find_modify(ptb, {'ipInfo.ip':task.get('body').get('ipInfo').get('ip'),'ipInfo.port':task.get('body').get('ipInfo').get('port'),'ipInfo.ptl':task.get('body').get('ipInfo').get('ptl')}, tempdata, True)
                    print ("验证完成:",task.get('body').get('ipInfo'))
                except Exception as e:
                    print (e)

    @classmethod
    def saver(cls):
        pass

    @classmethod
    def saver_server(cls, data, task):  # 运行在server端
        savedata = task['content']['body']['parsing_data']
        #mongodb.insert(savedata, 'jmProxy')

    @classmethod
    def get_next_time(cls):
        pass

    @classmethod
    def parser_run(cls):
        pass

if __name__ == '__main__':
    jpv = jm_task_proxyverificate()
    tasks = jpv.generateTask()
    print (tasks)