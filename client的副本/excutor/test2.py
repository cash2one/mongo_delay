
import asyncio,aiohttp

semaphore = asyncio.Semaphore(100)

async def aiohttp_lib(url):  #可用
    headers = {}
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36 vulners.com/bot'})
    conn = aiohttp.TCPConnector(verify_ssl=False,
                                limit=100,  # 连接池在windows下不能太大, <500
                                use_dns_cache=True)
    async with aiohttp.ClientSession(connector=conn, headers=headers) as session:
        try:
            async with session.get(url,timeout=100) as resp:
                print (resp.status)
                #if resp.status == 200:
                 #   print(resp.status)
                    #html = await resp.text()
                    #print (html)
                resp.release()
        except Exception as e:
            print('-->',e)
        session.close()
    conn.close()

async def aiohttp_inter():
    i = 0
    url = 'https://github.com'
    while True:
        i +=1
        if i <200:
            await aiohttp_lib(url)

tasks = []
for _ in range(0, 100):
    tasks.append(aiohttp_inter())  # 抓取任务
f = asyncio.wait(tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(f)