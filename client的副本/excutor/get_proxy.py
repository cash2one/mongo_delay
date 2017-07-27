from pymongo import  MongoClient
import time
def getdefaultproxy(self, tbobj):
    arr = tbobj.find({'ipInfo.status': 1, 'usetime': {'$lte': (time.time() - 5 * 60)}}, {'_id': 1})  # await
    idlist = []
    for myip in arr:
        idlist.append(myip.get('_id'))
    if len(idlist) <= 50:
        while True:
            try:
                mdfproxy = tbobj.find_and_modify(query={'ipInfo.status': 4},
                                                 update={'$set': {'ipInfo.count': 0, 'ipInfo.status': 1}})
                if mdfproxy is None:
                    break
            except Exception as e:
                print(e)
                break
    randomid = random.choice(idlist)
    proxyip = tbobj.find_and_modify(query={'_id': randomid},
                                    update={'$set': {'usetime': time.time()}, '$inc': {'ipInfo.count': 1}},
                                    new=True)  # 'ipInfo.status':1,'usetime':{'$lte':(time.time()-5*60)}
    if proxyip:
        if proxyip.get('ipInfo').get('count') >= 5 or proxyip.get('ipInfo').get('count') <= -5:
            tbobj.find_and_modify(query={'_id': proxyip.get('_id')}, update={'$set': {'ipInfo.status': 4}})
    return proxyip



conn = MongoClient('localhost', 27017, connect=False)
db = conn['jame_bd']  # 存储任务队列，任务队列，超时队列数据库
tb = db['jame_proxy1']  # 保存数据的数据库
a= tb.find_and_modify(query={},update={'$set':{'ipInfo.score.www_baidu_com.score':10000}},sort={'ipInfo.score.www_baidu_com.score':1})



def get_proxy(self, tbobj):  # 获取代理
    proxyip = tbobj.find_and_modify(query={'ipInfo.status': 1, 'usetime': {'$lte': (time.time() - 5 * 60)}},
                                          update={'$set': {'usetime': time.time()}, '$inc': {'ipInfo.count': 1}},
                                          )  # 'ipInfo.status':1,'usetime':{'$lte':(time.time()-5*60)}

    if proxyip:  # 得到代理
        return proxyip
    else:
        tbobj.update({'ipInfo.status': 4}, {'$set': {'ipInfo.count': 0, 'ipInfo.status': 1}})  # 将状态4的代理更新
        proxyip = tbobj.find_and_modify(
            query={'ipInfo.status': 1, 'usetime': {'$lte': (time.time() - 5 * 60)}},
            update={'$set': {'usetime': time.time()}, '$inc': {'ipInfo.count': 1}},
        )  # 'ipInfo.status':1,'usetime':{'$lte':(time.time()-5*60)}

    return proxyip







