## 📋 Day 24 — Quick Summary

### 🎯 Short Goal
Multiple tasks concurrently in Python using the threading module - covering how to create, start, and join threads, keep shared data safe with locks, and know when threading actually helps.

### 📚 Topics Covered
Threading basics, `threading.Thread()`, `.start()` and `.join()`, thread safety with `Lock()`, other safety tools (`RLock`, `Semaphore`, `Event`, `Queue`), when to use vs avoid threading, useful thread methods, and tips & tricks.


### 🔨 What I Learned


✅  **What threading is** — running multiple tasks concurrently using threads within a single program

✅  **`threading.Thread()`** — how to create a thread with a target function and arguments

✅  **`.start()`** — how to launch a thread to begin execution

✅  **`.join()`** — how to make the main thread wait for a thread to finish

✅  **Race conditions** — what goes wrong when threads share data unsafely

✅  **`threading.Lock()`** — how to protect shared data so only one thread accesses it at a time

✅  **Other safety tools** — `RLock`, `Semaphore`, `Event`, `Condition`, and `queue.Queue`

✅  **`queue.Queue()`** — the safest way to share data between threads

✅  **When to use threading** — best for I/O-bound tasks like network requests, file I/O, and API calls

✅  **When NOT to use threading** — avoid for CPU-bound tasks due to Python's **GIL**

✅  **Useful methods** — `is_alive()`, `active_count()`, `enumerate()`, `daemon`, and more


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

## ⏱️ Time Spent
~ 2.0 hrs