import asyncio
import requests
import logging
import time

start_time = time.time()


async def get(url):
    return requests.get(url)


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
logging.info('total time %s seconds', end_time - start_time)
