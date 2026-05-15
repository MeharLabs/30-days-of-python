## 📋 Day 25 — Quick Summary

### 🎯 Short Goal
Learn how to write non-blocking Python code using Async/Await to run multiple tasks concurrently.

### 📚 Topics Covered
Today you covered **Sync vs Async**, **async def functions**, the **await keyword**, **asyncio.run()**, **fetching multiple APIs asynchronously**, and essential asyncio tools like **gather, create_task, wait_for, sleep, as_completed, Lock, and Queue**.


### 🔨 What I Learned


✅ The difference between **sync** (blocking) and **async** (non-blocking) code

✅ How to define async functions using **`async def`**

✅ How to use the **`await`** keyword to pause and resume tasks

✅ How to launch async programs with **`asyncio.run()`**

✅ How to fetch **multiple APIs concurrently** instead of one by one

✅ How to run tasks at the same time using **`asyncio.gather()`**

✅ How to set timeouts with **`asyncio.wait_for()`**

✅ How to prevent race conditions using **`asyncio.Lock()`**

✅ How to limit concurrency with **`asyncio.Semaphore()`**

✅ How to use the **Producer/Consumer** pattern with `asyncio.Queue()`


## 🔑 Key Takeaways

- 🎯 Async is best for **I/O-bound tasks** like APIs, databases, and files — not CPU-heavy work
- 😴 Never use **`time.sleep()`** in async code — always use **`asyncio.sleep()`**
- ⚠️ Always **`await`** your coroutines — forgetting it returns an object, not the result
- 🌐 Use **`aiohttp`** instead of `requests` for async HTTP calls
- 🚀 **`asyncio.gather()`** is your best friend for running multiple tasks at once
- 🔒 Use **`Semaphore`** to avoid overwhelming APIs with too many requests
- 🏁 **`asyncio.run()`** should only be called **once** at the top level of your program
- 🧵 For CPU-bound blocking code, use **`run_in_executor()`** to avoid freezing the event loop


## ⏱️ Time Spent
~ 2.0 hrs