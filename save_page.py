import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(encoding='utf-8')


async def download(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)

        id_site = url.split('/')[4]
        file_name = f'site_cat{id_site}.html'
        with open(file_name, 'w') as f:
            f.write(html)


# Все страницы
urls = ['http://localhost:8000/category/1/',
        'http://localhost:8000/category/3/']


print('#' * 50)

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(download(url)) for url in urls]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)
