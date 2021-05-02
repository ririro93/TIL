import asyncio

async def fetch_data():
    print('start fetching data')
    await asyncio.sleep(2)
    print('data fetch complete')
    return {'data': 1}

async def number_count():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(number_count())

    val = await task1
    print(val)
    await task2
    print('all finished')

asyncio.run(main())
