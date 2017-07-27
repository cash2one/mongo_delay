import asyncio,aiohttp
async def test():
    await asyncio.sleep(0)
    print ('*****')

async def befor():
    while True:
        print ('+++--+++')
        await asyncio.sleep(0)#模拟得到任务
        tasks = []
        for i in range(100):
            tasks.append(test())  # 将任务分解为单个抓取任务
        f = asyncio.wait(tasks)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(f)
        loop.close()


async def aio_http():
    i= 0
    while True:
        i +=1
        if i<200:
            async with aiohttp.get('https://github.com')  as resp:
                print(resp.status)
                print(await resp.text())
                resp.release()

tasks = []
"""
for i in range(100):
    tasks.append(aio_http())  # 将任务分解为单个抓取任务
"""
tasks.append(befor())
f = asyncio.wait(tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(f)
loop.close()