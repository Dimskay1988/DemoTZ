import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json



async def get_page(session, url):
    async with session.get(url, ssl=False) as r:
        return await r.text()


async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data


def parser(results):
    for r in results:
        html = json.loads(r)
        data = {
            'article': html.get('nm_id'),
            'brand': html.get('imt_name'),
            'title': html.get('description')
        }
        print(data)
    return


if __name__ == '__main__':
    urls = [
        # 'https://www.wildberries.ru/catalog/73512949/detail.aspx',
        # 'https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json'
        # f'https://basket-05.wb.ru/vol735/part73512/{article}/info/ru/card.json'
            ]

    results = asyncio.run(main(urls))
    parser(results)

