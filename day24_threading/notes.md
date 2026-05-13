# 🧵 Day 24 – Python Threading


## 🎯 Goal

Run multiple tasks concurrently in Python using the `threading` module — covering how to create, start, and join threads, keep shared data safe with locks, and know when threading actually helps.


## 🤔 What is Threading?

**Threading** is a way to run **multiple tasks concurrently** within a single program. A **thread** is the smallest unit of execution in a process.

> 🍽️ Think of your program as a restaurant. The **main process** is the restaurant itself, and each **thread** is a different waiter handling multiple tables *at the same time*.

Python uses the built-in `threading` module to create and manage threads.

```python
import threading
```

### 🧠 Process vs Thread

| Feature | Process | Thread |
|---|---|---|
| Memory | Separate memory space | Shared memory space |
| Speed | Slower to create | Faster to create |
| Communication | Harder (IPC needed) | Easier (shared data) |
| Crash impact | Isolated | Can crash whole program |

---

## 🏗️ `threading.Thread()`

The **core class** used to create a new thread.

### ✅ Syntax

```python
t = threading.Thread(target=function_name, args=(arg1, arg2))
```

### 📌 Parameters

| Parameter | Description |
|---|---|
| `target` | The function the thread will run |
| `args` | Tuple of positional arguments |
| `kwargs` | Dictionary of keyword arguments |
| `name` | Optional name for the thread |
| `daemon` | If `True`, thread dies when main program exits |

### 🔍 Example

```python
import threading

def greet(name):
    print(f"Hello, {name}! 👋")

t = threading.Thread(target=greet, args=("Alice",))
```


## ▶️ `.start()` and `.join()`

### 🟢 `.start()`
- **Launches** the thread — tells Python *"go run this now"*
- The thread begins executing its `target` function
- Returns immediately (non-blocking for the main thread)

```python
t.start()  # 🚀 Thread begins running
```

### 🔴 `.join()`
- **Waits** for the thread to finish before continuing
- Blocks the calling thread until the target thread completes
- Prevents the main program from exiting early

```python
t.join()  # ⏳ Main thread waits here until t is done
```

### 🔍 Full Example

```python
import threading
import time

def task(name, delay):
    time.sleep(delay)
    print(f"✅ Task {name} done!")

t1 = threading.Thread(target=task, args=("A", 2))
t2 = threading.Thread(target=task, args=("B", 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("🎉 All tasks completed!")

# Output:
# ✅ Task B done!   ← finishes first (1 sec)
# ✅ Task A done!   ← finishes second (2 sec)
# 🎉 All tasks completed!
```


## 🛡️ Thread Safety Basics

When multiple threads **share the same data**, things can go **horribly wrong** 😱. This is called a **race condition**.

### 💥 Race Condition (UNSAFE)

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # ⚠️ Not thread-safe!

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start(); t2.start()
t1.join();  t2.join()

print(counter)  # ❌ Expected 200000, but you'll get something random!
```

### 🔒 `threading.Lock()` — The Fix

A **Lock** ensures only **one thread** accesses a resource at a time.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:           # 🔒 Only one thread at a time
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start(); t2.start()
t1.join();  t2.join()

print(counter)  # ✅ Always 200000
```

### 🧰 Other Thread Safety Tools

| Tool | Use Case |
|---|---|
| `threading.Lock()` | Basic mutual exclusion (one thread at a time) |
| `threading.RLock()` | Re-entrant lock (same thread can acquire multiple times) |
| `threading.Semaphore()` | Allow N threads at a time (e.g. max 3 DB connections) |
| `threading.Event()` | Signal between threads (wait/notify) |
| `threading.Condition()` | Advanced wait/notify with a lock |
| `queue.Queue()` | Thread-safe data sharing between threads |

### 📡 `threading.Event()` Example

```python
import threading, time

event = threading.Event()

def worker():
    print("⏳ Worker waiting for signal...")
    event.wait()       # Blocks until event is set
    print("🚀 Worker received signal, starting!")

t = threading.Thread(target=worker)
t.start()

time.sleep(2)
event.set()   # 📣 Signal the worker to proceed
t.join()
```

### 📦 `queue.Queue()` — Safe Data Sharing

```python
import threading
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)               # 📥 Put item in queue
        print(f"Produced: {i}")

def consumer():
    while True:
        item = q.get()         # 📤 Get item from queue
        if item is None:
            break
        print(f"Consumed: {item} ✅")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start(); t2.start()
t1.join()
q.put(None)   # 🛑 Signal consumer to stop
t2.join()
```


## ⏰ When to Use Threading

### ✅ USE Threading For — I/O-Bound Tasks

| Scenario | Example |
|---|---|
| 🌐 Network requests | Fetching multiple URLs simultaneously |
| 📁 File I/O | Reading/writing multiple files |
| 🗄️ Database queries | Running multiple DB queries at once |
| ⌨️ User input | Listening for input while doing background work |
| 🔌 API calls | Hitting multiple APIs concurrently |

```python
# ✅ Great use case: fetching multiple URLs
import threading, requests

urls = ["https://api1.com", "https://api2.com", "https://api3.com"]

def fetch(url):
    response = requests.get(url)
    print(f"Got {len(response.content)} bytes from {url}")

threads = [threading.Thread(target=fetch, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()
```

### ❌ DON'T Use Threading For — CPU-Bound Tasks

| Scenario | Why Not | Use Instead |
|---|---|---|
| 🔢 CPU-heavy math | GIL blocks true parallelism | `multiprocessing` |
| 🖼️ Image processing | CPU-bound, threads won't help | `multiprocessing` |
| 🤖 ML model training | Needs real parallel CPU cores | `multiprocessing` / GPU |

> 🐍 **The GIL (Global Interpreter Lock):** Python's GIL allows only **one thread to execute Python bytecode at a time**. Threading doesn't give true CPU parallelism — but it still helps massively for **I/O-bound** tasks where threads spend time *waiting*, not *computing*.


## 🧰 Useful Threading Methods & Properties

```python
t = threading.Thread(target=fn)
```

| Method / Property | Description |
|---|---|
| `t.start()` | Start the thread |
| `t.join(timeout)` | Wait for thread to finish (optional timeout) |
| `t.is_alive()` | Returns `True` if thread is still running |
| `t.name` | Get or set the thread's name |
| `t.ident` | Thread's unique ID (set after `.start()`) |
| `t.daemon` | If `True`, dies when main thread dies |
| `threading.current_thread()` | Returns the currently running thread |
| `threading.active_count()` | Number of currently alive threads |
| `threading.enumerate()` | List of all alive threads |

---

## 💡 Tips & Tricks

- 🧵 Use `threading` for **I/O-bound** work, `multiprocessing` for **CPU-bound** work
- 🔒 Always use **locks or queues** when sharing mutable data between threads
- 👻 Set `daemon=True` for **background threads** that should die with the main program
- 📦 Prefer `queue.Queue` over shared variables — it's **always thread-safe**
- ⚠️ Avoid **global state** in threaded programs whenever possible
- 🔍 Use `t.is_alive()` to **check status** without blocking
- ⏱️ Use `t.join(timeout=5)` to **avoid hanging forever** if a thread gets stuck
- 🧪 Test threaded code with **stress tests** — race conditions are non-deterministic!

---

## 🗺️ Threading Mental Model

```
Main Thread
    │
    ├──► Thread 1 ──► [I/O task] ──► done ──┐
    ├──► Thread 2 ──► [I/O task] ──► done ──┤
    └──► Thread 3 ──► [I/O task] ──► done ──┘
                                             │
                                    All .join() ──► Continue
```


## 📝 What I Learned

- 🤔 **What threading is** — running multiple tasks concurrently using threads within a single program
- 🏗️ **`threading.Thread()`** — how to create a thread with a target function and arguments
- ▶️ **`.start()`** — how to launch a thread to begin execution
- ⏳ **`.join()`** — how to make the main thread wait for a thread to finish
- 💥 **Race conditions** — what goes wrong when threads share data unsafely
- 🔒 **`threading.Lock()`** — how to protect shared data so only one thread accesses it at a time
- 🧰 **Other safety tools** — `RLock`, `Semaphore`, `Event`, `Condition`, and `queue.Queue`
- 📦 **`queue.Queue()`** — the safest way to share data between threads
- ⏰ **When to use threading** — best for I/O-bound tasks like network requests, file I/O, and API calls
- ❌ **When NOT to use threading** — avoid for CPU-bound tasks due to Python's **GIL**
- 🛠️ **Useful methods** — `is_alive()`, `active_count()`, `enumerate()`, `daemon`, and more

---

## 🔑 Key Takeaways

- 🧵 Threading lets you run tasks **concurrently**, not truly in parallel in Python
- 🐍 The **GIL** limits threading to **I/O-bound** tasks only — not CPU-heavy work
- 🔒 **Always protect shared data** with `Lock()` or you'll get unpredictable results
- 📦 **`queue.Queue()`** is the safest and cleanest way to pass data between threads
- 🚀 `.start()` launches the thread, ⏳ `.join()` waits for it to finish — always use both
- 👻 Use `daemon=True` for background threads that should die with the main program
- ❌ For CPU-bound tasks, use **`multiprocessing`** instead of threading
- 🧪 Race conditions are **non-deterministic** — always stress test threaded code
- ⏱️ Use `t.join(timeout=5)` to avoid your program **hanging forever**
- ✅ Threading shines most when your tasks spend time **waiting** — not computing