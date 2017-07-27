#根据类型对应相应的存储接口

import setting
import itertools
class save_Data:
    def __init__(self):
        pass

    @classmethod
    def getolddata(cls, task, obj_db):
        proxyip = None
        ip = task.get('data').get('ipInfo').get('ip')
        port = task.get('data').get('ipInfo').get('port')
        ptl = task.get('data').get('ipInfo').get('ptl')
        tb = obj_db.chocie_db_tb(setting.TMP_DB, 'jm_task_proxyverificate') #根据上传数据的任务类型进行分表

        arr = obj_db.find_data(tb,{'data.ipInfo.ip': ip, 'data.ipInfo.port': port, 'data.ipInfo.ptl': ptl})
        for myip in arr:
            proxyip = myip
        return proxyip

    @classmethod
    def getzuselist(cls, oldlist, newlist):
        nzlist = []
        zlist = oldlist + newlist
        zlist.sort(key=lambda temp: temp['time'])
        it = itertools.groupby(zlist)
        for k, g in it:
            nzlist.append(k)
        listlen = len(nzlist)
        if listlen > 100:
            for _ in range(listlen - 100):
                del nzlist[0]
        return nzlist

    @classmethod
    def getzscorecords(cls, olddata, newdata):
        tempdata = olddata
        zret = olddata
        for k, v in newdata.items():
            tempdict = {}
            if k in olddata.keys():
                tmp = tempdata.get(k)
                tempdict['useInterval'] = tmp.get('useInterval', 300)
                tempdict['transV'] = tmp.get('transV', 0)
                tempdict['resTime'] = v.get('resTime')
                tempdict['lastTime'] = v.get('lastTime')
                tempdict['score'] = tempdata.get('score', 0) + v.get('score', 0)
                tempdict['suscount'] = tempdata.get('suscount', 0) + v.get('suscount', 0)
                tempdict['usecount'] = tempdata.get('usecount', 0) + v.get('usecount', 0)
                zret[k] = tempdict
        return zret

    @classmethod
    def getzverifitasks(cls, olddata, newdata):
        tempdata = olddata
        zret = olddata
        for k, v in newdata.items():
            tempdict = {}
            if k in olddata.keys():
                tmp = tempdata.get(k)
                tempdict['interval'] = tmp.get('interval', 60 * 60 * 24)
                tempdict['timeout'] = tmp.get('timeout', 300)
                tempdict['status'] = tmp.get('status', 0)
                tempdict['lastTime'] = v.get('lastTime')
                tempdict['passcount'] = tmp.get('passcount', 0) + v.get('passcount', 0)
                tempdict['taskcount'] = tmp.get('taskcount', 0) + v.get('taskcount', 0)
                zret[k] = tempdict
        return zret

    @classmethod
    def saver_server(cls, newdata, obj_db):  # 运行在server端#obj_db为代理的表的对象
        olddata = cls.getolddata(newdata, obj_db)
        if olddata is None:

            return

        # 使用记录合并
        olduselist = olddata.get('data').get('ipInfo').get('use')
        newuselist = newdata.get('data').get('ipInfo').get('use')
        zuselist = cls.getzuselist(olduselist, newuselist)
        # 打分记录合并
        oldscorerecords = olddata.get('data').get('ipInfo').get('score')
        newscorerecords = olddata.get('data').get('ipInfo').get('score')
        zscorerecords = cls.getzscorecords(oldscorerecords, newscorerecords)
        # 验证任务记录合并
        oldverifitasks = olddata.get('data').get('ipInfo').get('task').get('verifi')
        newverifitasks = olddata.get('data').get('ipInfo').get('task').get('verifi')
        zverifitasks = cls.getzverifitasks(oldverifitasks, newverifitasks)
        olddata['data']['ipInfo']['use'] = zuselist
        olddata['data']['ipInfo']['score'] = zscorerecords
        olddata['data']['ipInfo']['task']['verifi'] = zverifitasks
        cls.updateproxy(olddata, obj_db)


    @classmethod
    def updateproxy(cls, mydata, obj_db):
        ip = mydata.get('data').get('ipInfo').get('ip')
        port = mydata.get('data').get('ipInfo').get('port')
        ptl = mydata.get('data').get('ipInfo').get('ptl')
        tb = obj_db.chocie_db_tb(setting.TMP_DB, 'jm_task_proxyverificate')  # 根据上传数据的任务类型进行分表
        obj_db.find_modify(tb,{'data.ipInfo.ip': ip, 'data.ipInfo.port': port, 'data.ipInfo.ptl': ptl},mydata)


    def jm_task_proxyverificate(self,obj_db,tb,data):# 参数1数据库操作对象，参数2为存储的数据表，参数3为存储的数据
        pass

    def jd_task_kind(self,obj_db,tb,data):# 二级页面存储接口
        obj_db.insert_data(tb,data)


