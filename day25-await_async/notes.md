# Day 25 — Async / Await in Python 🐍⚡

## 🎯 Goal

Understand **Async/Await in Python** — learning how asynchronous code works, the difference between sync and async execution, how to define and use `async def` functions with the `await` keyword, how to launch async programs using `asyncio.run()`, and how to fetch multiple APIs concurrently to write faster, non-blocking Python code.


## 📚 Topics Covered


## 🤔 What is Async / Await?

**Async/Await** is a way to write **asynchronous code** in Python — code that can **pause and resume** without blocking everything else. Instead of waiting for one task to finish before starting the next, async lets you juggle multiple tasks at once.

> 💡 Think of it like a chef cooking multiple dishes simultaneously — not waiting for pasta to boil before chopping vegetables.


## 🔄 Sync vs Async — The Core Difference

### 😴 Synchronous (Blocking)

```python
import time

def make_coffee():
    print("☕ Boiling water...")
    time.sleep(3)          # BLOCKS everything for 3 seconds
    print("☕ Coffee ready!")

def make_toast():
    print("🍞 Toasting bread...")
    time.sleep(2)          # BLOCKS everything for 2 seconds
    print("🍞 Toast ready!")

make_coffee()   # waits 3s
make_toast()    # then waits 2s
# Total: ~5 seconds ❌ Slow
```

### ⚡ Asynchronous (Non-Blocking)

```python
import asyncio

async def make_coffee():
    print("☕ Boiling water...")
    await asyncio.sleep(3)   # pauses, lets others run
    print("☕ Coffee ready!")

async def make_toast():
    print("🍞 Toasting bread...")
    await asyncio.sleep(2)   # pauses, lets others run
    print("🍞 Toast ready!")

async def main():
    await asyncio.gather(make_coffee(), make_toast())

asyncio.run(main())
# Total: ~3 seconds ✅ Fast!
```

| Feature | Sync | Async |
|---|---|---|
| ⏱️ Execution | One at a time | Concurrent |
| 🚫 Blocking | Yes | No |
| 🧵 Threads needed | Often yes | No |
| 🎯 Best for | CPU tasks | I/O tasks (API, DB, files) |

---

## 🔧 `async def` — Defining Async Functions

An `async def` function is called a **coroutine**. It doesn't run immediately — it returns a coroutine object that must be **awaited**.

```python
# ✅ Defining a coroutine
async def greet(name):
    print(f"👋 Hello, {name}!")
    await asyncio.sleep(1)
    return f"Done greeting {name}"

# ❌ Calling it normally does NOTHING useful
greet("Ali")  # Just creates coroutine object, doesn't run it

# ✅ You must await it or run it
async def main():
    result = await greet("Ali")
    print(result)
```

### 🧠 Key Rules

```python
# ✅ async def → must be awaited
# ✅ await → only inside async def
# ❌ Can't use await in regular functions

def regular():
    await something()  # 🚨 SyntaxError!

async def correct():
    await something()  # ✅ Works!
```

---

## ⏳ `await` — The Pause Button

`await` tells Python: *"Pause here, go do other things, come back when this is done."*

```python
import asyncio

async def fetch_data(source, delay):
    print(f"📡 Fetching from {source}...")
    await asyncio.sleep(delay)    # ← pause point
    print(f"✅ Got data from {source}!")
    return f"Data from {source}"

async def main():
    result = await fetch_data("Database", 2)
    print(result)

asyncio.run(main())
```

### ✅ What you can `await`

| Awaitable | Example |
|---|---|
| 🔁 Coroutines | `await my_async_func()` |
| 📦 Tasks | `await asyncio.create_task(...)` |
| 🔮 Futures | `await some_future` |
| 🌐 HTTP (aiohttp) | `await session.get(url)` |
| 🗄️ DB (asyncpg) | `await conn.fetch(query)` |

---

## 🚀 `asyncio.run()` — The Entry Point

`asyncio.run()` is the **main launcher** for async programs. It creates an event loop, runs your coroutine, then closes the loop.

```python
import asyncio

async def main():
    print("🚀 Starting async program")
    await asyncio.sleep(1)
    print("🏁 Done!")

# ✅ The proper way to start async code
asyncio.run(main())
```

### ⚠️ Important Notes

```python
# ✅ Call asyncio.run() ONCE at the top level
asyncio.run(main())

# ❌ Don't call it inside an async function
async def bad():
    asyncio.run(other())   # 🚨 RuntimeError!

# ✅ Inside async, just await instead
async def good():
    await other()          # ✅ Correct
```

---

## 🌐 Fetching Multiple APIs Async

This is where async **truly shines** — making many API calls concurrently instead of one by one.

### 😴 The Slow Way (Sync)

```python
import requests

urls = [
    "https://api.example.com/user/1",
    "https://api.example.com/user/2",
    "https://api.example.com/user/3",
]

for url in urls:
    response = requests.get(url)  # waits each time
    print(response.json())
# Takes: 3 × 2s = 6 seconds 🐌
```

### ⚡ The Fast Way (Async with aiohttp)

```python
import asyncio
import aiohttp   # pip install aiohttp

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]

async def fetch(session, url):
    async with session.get(url) as response:   # ← async context manager
        data = await response.json()
        print(f"✅ Got: {data['title'][:40]}")
        return data

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)   # ← run ALL at once
        return results

async def main():
    print("🚀 Fetching all APIs concurrently...")
    results = await fetch_all(urls)
    print(f"📦 Total fetched: {len(results)} posts")

asyncio.run(main())
# Takes: ~1-2s total instead of 5× sequential 🚀
```

---

## 🛠️ Essential asyncio Methods & Tools

### 📦 `asyncio.gather()` — Run tasks concurrently

```python
async def main():
    # ✅ Run multiple coroutines AT THE SAME TIME
    results = await asyncio.gather(
        fetch("API 1"),
        fetch("API 2"),
        fetch("API 3"),
    )
    print(results)  # List of all results

    # ✅ Handle errors individually with return_exceptions
    results = await asyncio.gather(
        fetch("Good API"),
        fetch("Bad API"),
        return_exceptions=True   # won't crash on one failure
    )
```

### 🏃 `asyncio.create_task()` — Schedule background tasks

```python
async def main():
    # ✅ Creates a Task — starts running in background immediately
    task1 = asyncio.create_task(fetch("API 1"))
    task2 = asyncio.create_task(fetch("API 2"))

    print("📌 Tasks scheduled, doing other work...")

    result1 = await task1   # wait for result when needed
    result2 = await task2
```

### ⏰ `asyncio.wait_for()` — Add a timeout

```python
async def main():
    try:
        # ✅ Cancel if takes longer than 5 seconds
        result = await asyncio.wait_for(
            fetch_slow_api(),
            timeout=5.0
        )
    except asyncio.TimeoutError:
        print("⏰ Request timed out!")
```

### 🔁 `asyncio.sleep()` — Async pause (not blocking!)

```python
async def countdown():
    for i in range(5, 0, -1):
        print(f"⏳ {i}...")
        await asyncio.sleep(1)   # ✅ async-friendly, not time.sleep()
    print("🚀 Go!")
```

### 📋 `asyncio.as_completed()` — Process results as they arrive

```python
async def main():
    tasks = [fetch(url) for url in urls]

    # ✅ Process each result as SOON as it's done (not waiting for all)
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"🎯 First done: {result}")
```

### 🔒 `asyncio.Lock()` — Prevent race conditions

```python
lock = asyncio.Lock()
shared_counter = 0

async def safe_increment():
    global shared_counter
    async with lock:           # ✅ Only one coroutine at a time
        shared_counter += 1
        await asyncio.sleep(0.1)
```

### 📬 `asyncio.Queue()` — Producer/Consumer pattern

```python
async def producer(queue):
    for i in range(5):
        await queue.put(f"Task {i}")   # ✅ put items in
        print(f"📤 Produced: Task {i}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item = await queue.get()        # ✅ get items out
        print(f"📥 Consumed: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )
```


## 🎯 Tips & Tricks

### ✅ DO's

```python
# 1️⃣ Always use asyncio.sleep() not time.sleep() in async code
await asyncio.sleep(1)     # ✅ Non-blocking
time.sleep(1)              # ❌ Blocks everything!

# 2️⃣ Use gather() for concurrent tasks
await asyncio.gather(task1(), task2(), task3())   # ✅

# 3️⃣ Use async context managers for resources
async with aiohttp.ClientSession() as session:    # ✅ auto-closes
    ...

# 4️⃣ Use async for for async iterators
async for item in async_generator():              # ✅
    process(item)

# 5️⃣ Handle timeouts explicitly
await asyncio.wait_for(risky_call(), timeout=10)  # ✅
```

### ❌ DON'Ts

```python
# 1️⃣ Don't block the event loop
def slow_cpu_task():
    time.sleep(5)          # ❌ Freezes ALL async tasks

# 2️⃣ Don't forget to await coroutines
result = fetch_data()      # ❌ Returns coroutine, not data!
result = await fetch_data() # ✅

# 3️⃣ Don't use asyncio.run() inside async functions
async def bad():
    asyncio.run(other())   # ❌ RuntimeError

# 4️⃣ Don't mix sync blocking I/O in async code
async def bad():
    data = requests.get(url)   # ❌ Blocks event loop!
    data = await aiohttp...    # ✅ Use async libraries
```

### 🚀 Pro Tips

```python
# 💡 Tip 1: Run sync blocking code in a thread pool
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def run_blocking():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_func)

# 💡 Tip 2: Limit concurrency with Semaphore (avoid overwhelming APIs)
semaphore = asyncio.Semaphore(10)   # max 10 concurrent requests

async def limited_fetch(url):
    async with semaphore:
        return await fetch(url)

# 💡 Tip 3: asyncio.TaskGroup (Python 3.11+) — cleaner task management
async def main():
    async with asyncio.TaskGroup() as tg:    # ✅ Modern way
        task1 = tg.create_task(fetch("API 1"))
        task2 = tg.create_task(fetch("API 2"))
    # All tasks done here, errors propagate cleanly
```


## 🗺️ Quick Reference Cheatsheet

```
asyncio ecosystem
├── 🔁 Core
│   ├── async def       → define coroutine
│   ├── await           → pause & resume
│   ├── asyncio.run()   → start event loop
│   └── asyncio.sleep() → async pause
│
├── 📦 Concurrency
│   ├── asyncio.gather()        → run all, wait for all
│   ├── asyncio.create_task()   → schedule background task
│   ├── asyncio.as_completed()  → process as they finish
│   └── asyncio.wait()          → fine-grained task control
│
├── ⏱️ Control
│   ├── asyncio.wait_for()  → timeout wrapper
│   ├── asyncio.shield()    → protect from cancellation
│   └── task.cancel()       → cancel a running task
│
├── 🔒 Synchronization
│   ├── asyncio.Lock()      → mutual exclusion
│   ├── asyncio.Semaphore() → limit concurrency
│   ├── asyncio.Event()     → signal between coroutines
│   └── asyncio.Queue()     → producer/consumer
│
└── 🌐 Popular Async Libraries
    ├── aiohttp     → HTTP requests
    ├── asyncpg     → PostgreSQL
    ├── aiofiles    → File I/O
    ├── fastapi     → Web framework
    └── motor       → MongoDB
```

> 🧠 **Golden Rule:** Async is perfect for **I/O-bound** tasks (network, files, DB). For **CPU-bound** tasks (math, image processing), use `multiprocessing` instead!

---

## ✅ What I Learned

- ⚡ The difference between **sync** (blocking) and **async** (non-blocking) code
- 🔧 How to define async functions using **`async def`**
- ⏳ How to use the **`await`** keyword to pause and resume tasks
- 🚀 How to launch async programs with **`asyncio.run()`**
- 🌐 How to fetch **multiple APIs concurrently** instead of one by one
- 📦 How to run tasks at the same time using **`asyncio.gather()`**
- ⏰ How to set timeouts with **`asyncio.wait_for()`**
- 🔒 How to prevent race conditions using **`asyncio.Lock()`**
- 🚦 How to limit concurrency with **`asyncio.Semaphore()`**
- 📬 How to use the **Producer/Consumer** pattern with `asyncio.Queue()`

---

## 🧠 Key Takeaways

- 🎯 Async is best for **I/O-bound tasks** like APIs, databases, and files — not CPU-heavy work
- 😴 Never use **`time.sleep()`** in async code — always use **`asyncio.sleep()`**
- ⚠️ Always **`await`** your coroutines — forgetting it returns an object, not the result
- 🌐 Use **`aiohttp`** instead of `requests` for async HTTP calls
- 🚀 **`asyncio.gather()`** is your best friend for running multiple tasks at once
- 🔒 Use **`Semaphore`** to avoid overwhelming APIs with too many requests
- 🏁 **`asyncio.run()`** should only be called **once** at the top level of your program
- 🧵 For CPU-bound blocking code, use **`run_in_executor()`** to avoid freezing the event loop