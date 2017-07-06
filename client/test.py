#该脚本负责启动其他脚本，并且监控程序的执行情况，主要是zmq与服务器的连接情况，检查到与服务器失去连接将重启客户端代码

#此脚本只适用于linux系统


import sys,os,time
import setting
from pymongo import  MongoClient

class check_connect_status:
    def __init__(self):
        conn = MongoClient('localhost', 27017, connect=False)
        self.db = conn[setting.DATABASES]
        self.local_task = self.db['local_task_ready_list']#进入本地与服务器交互的就绪任务列表
    def select_table(self, table):  # 查表，并删除第一个查询到的数据
        tb = self.db[table]
        data = tb.find_and_modify(query={},remove=True)
        return data

    def get_check_task(self):#如果有检查任务代表需要检查客户端与服务器的交互就绪任务列表，如果就绪列表在个数大于某个数不减少，则认为断链
        topic = 'local_check_task'
        queued_name = topic + '_ready_list'  # 表   根据类型拼接到自己类型所在的就绪任务队列
        while True:
            data = self.select_table(queued_name)  # 得到任务，实际上的真实数据为任务id，并且将就绪列表的id删除
            if data:
                return self.local_task.count()#得到本地与服务器交互的本地任务列表数
            else:
                time.sleep(1)

    def kill_process_by_name(self,name):#杀死进程的方法
        cmd = "ps -e | grep %s" % name
        f = os.popen(cmd)
        txt = f.readlines()
        print (txt)
        if len(txt) == 0:
            print ("no process \"%s\"!!" % name)
            return
        else:
           for line in txt:
               colum = line.split()
               pid = colum[0]
               cmd = "kill -9 %d" % int(pid)
               rc = os.system(cmd)
               if rc == 0 :
                   print ("exec \"%s\" success!!" % cmd)
               else:
                   print ("exec \"%s\" failed!!" % cmd)
        return



def run():
    count = 0
    obj = check_connect_status()
    local_count = obj.get_check_task()
    if local_count >= 2:
        count +=1
    obj.kill_process_by_name('python')#杀死进程



if __name__ == "__main__":
    name = 'python'#负责杀死进程名为python的进程
    #kill_process_by_name(name)

