# ============================================
# 🐍 Day 25 - Async / Await
# 📅 Date: 14/05/2026
# 🎯 Goal: Learn how to write non-blocking Python code using Async/Await to run multiple tasks concurrently.
# =============================================

# --- code starts from here ---

import aiohttp
import asyncio


async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data": "Some data"}


async def main():
    print("Start of main coroutine")
    task = fetch_data(2)

    result = await task

    print(f"Received result: {result}")
    print("End of main coroutine")


asyncio.run(main())


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())


async def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            print("Title:", data["title"])
            print("Body:", data["body"])


asyncio.run(fetch_post())
