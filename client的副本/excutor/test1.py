
import motor.motor_asyncio
import asyncio,random,time
import socket
class hhhhh:
    def __init__(self):
        # 存放抓取任务的数据库
        conn = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017, connect=False)
        pdb = conn['jame_bd']
        self.ptable = pdb['jame_proxy']
        self.url_q = asyncio.Queue()
        self.tmp = []
        a = 'sddsaadsadasdadawweqewqwqeqwewqeqwwqeqewqeqwqeqweqeqqweqqqeeqwewqewewrrfdfdsffdsfsdd'
        for i in range(1000):
            self.tmp.append(a)
    def run(self):
        tasks = []
        tasks.append(self.put_q())  # 将同一任务分解的单个抓取任务得到的数据拼接为一个解析任务
        for i in range(100):
            tasks.append(self.get_q())
        f = asyncio.wait(tasks)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f)
        self.url_q.join()

    async def get_q(self): #获取代理
        while True:
            print ('get')
            try:
                url =await self.url_q.get()
                self.url_q.task_done()
            except Exception as e:
                print ('***',e)


    async def put_q(self):#将任务分解为单个抓取任务
        while True:
            await asyncio.sleep(0)
            a = await self.ptable.find_one()
            print (a)
            await self.url_q.put(a)  # 将url添加到队列


if __name__ == '__main__':
    obj = hhhhh()
    obj.run()
