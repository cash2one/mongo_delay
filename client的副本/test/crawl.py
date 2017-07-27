# _*_ coding: utf-8 _*_
# @Time    : 2017/5/12 上午9:31
# @Author  : Strongc
# @Author_Email   : qncz2006 # gmail dot com
# @Explain :
# @File    : Crawl4.py
# @Software: PyCharm Community Edition

import asyncio

import aiohttp
# import tqdm
import zmq
from aiocfscrape import CloudflareScraper


class JM_Crawl(object):
    def __init__(self):
        context_recv = zmq.Context()
        self.socket_recv = context_recv.socket(zmq.PULL)
        self.socket_recv.bind("tcp://*:5550")

        context_send = zmq.Context()
        self.socket_send = context_send.socket(zmq.PUSH)
        self.socket_send.bind("tcp://*:5551")

        self.poller = zmq.Poller()
        self.poller.register(self.socket_recv, zmq.POLLIN)

        self.semaphore = asyncio.Semaphore(100)

        self.loop = asyncio.get_event_loop()
        self.url_q = asyncio.Queue()
        self.result_q = asyncio.Queue()

        self.workcount = 0
        self.count = 0

    def run(self):

        tasks = []
        tasks.append(self.get_zmq())
        tasks.append(self.send_zmq())
        for _ in range(0, 200):
            tasks.append(self.work())

        f = asyncio.wait(tasks)
        self.loop.run_until_complete(f)

        self.url_q.join()
        self.result_q.join()

    async def work(self):
        print('Work start')
        self.workcount += 1
        while True:
            """
            if self.count >= 2000:
                self.workcount -= 1
                break
            """
            await asyncio.sleep(0)
            url = await self.get_url()
            if url:
                await self.parseUrl(url)

    async def get_zmq(self):

        while True:
            """
            if self.count > -1999 and self.workcount <= 0:
                break
            """
            socks = dict(self.poller.poll(0.1))
            if self.socket_recv in socks and socks[self.socket_recv] == zmq.POLLIN:
                url = self.socket_recv.recv_pyobj()
                if url:
                    # print(url)
                    await self.url_q.put(url['url'])
                else:
                    await asyncio.sleep(0.1)
            else:
                await asyncio.sleep(0.1)

    async def get_url(self):
        url = await self.url_q.get()
        print(url)
        return url

    async def send_zmq(self):
        while True:
            """
            if self.count > -1999 and self.workcount <= 0:
                break
            """
            html, url = await self.result_q.get()
            self.socket_send.send_pyobj({'html': html, 'url': url})
            self.result_q.task_done()

    async def sendhtml(self, html, url):
        print('done.....', url)
        await self.result_q.put((html, url))
        self.count += 1

    async def parseUrl(self, url):
        cloudflare = False
        if cloudflare:
            sessionClient = CloudflareScraper
        else:
            sessionClient = aiohttp.ClientSession

        conn = aiohttp.TCPConnector(verify_ssl=False,
                                    limit=100,  # 连接池在windows下不能太大, <500
                                    use_dns_cache=True)
        headers = {}
        headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36 vulners.com/bot'})

        async with sessionClient(connector=conn, headers=headers) as session:
            async with (self.semaphore):
                try:
                    await self.get(session, url, 10, False)
                except Exception as e:
                    print('Failed....', e, url)
                    # return page

    async def get(self, session, url, timeout, rawResult, maxRetry=5):
        currentTry = 1
        print(url)
        while (currentTry < maxRetry):
            try:
                response = await session.get(url.strip(), timeout=timeout)
                if response.status == 200:
                    if rawResult:
                        result = await response.read()
                    else:
                        result = await response.text()
                    # print(result['url'])
                    self.url_q.task_done()
                    await self.sendhtml(result, url)
                    response.release()
                    return
                else:
                    response.release
            except Exception as e:
                currentTry += 1
                if currentTry > maxRetry:
                    print('Get error', e)
                    raise e


if __name__ == "__main__":
    import cProfile

    crawl = JM_Crawl()
    cProfile.run("crawl.run()", filename="Crawl46_profile.out")