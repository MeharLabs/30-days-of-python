# 🐍 Day 17 — Python Generators

## 🎯 Goal

Understand how to use `yield`, generator functions, and expressions to write **memory-efficient, lazy, and clean Python code** that produces values on demand instead of all at once.


## 🔍 What Are Generators?

Generators are a special type of **iterator** in Python that let you **produce values one at a time**, pausing execution between each value instead of computing everything at once. They are defined like normal functions but use the `yield` keyword instead of `return`.

Think of a generator like a **lazy factory** 🏭 — it only produces an item when you ask for it, not all at once.

```python
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```


## ⚡ The `yield` Keyword

`yield` is the heart of any generator. It **pauses** the function, saves its state, and **sends a value back** to the caller. When called again, it resumes right where it left off.

```python
def countdown(n):
    while n > 0:
        yield n       # Pause here, send n to caller
        n -= 1        # Resume from here on next call

for num in countdown(5):
    print(num)        # 5, 4, 3, 2, 1
```

### 🆚 `yield` vs `return`

| Feature | `return` | `yield` |
|---|---|---|
| Exits function? | ✅ Yes, permanently | ❌ No, just pauses |
| Produces iterator? | ❌ No | ✅ Yes |
| Remembers state? | ❌ No | ✅ Yes |
| Multiple values? | ❌ One value | ✅ Many values |

> 💡 **Tip:** A function with even **one** `yield` becomes a generator function automatically!

---

## 🏭 Generator Functions

A **generator function** looks like a normal function but returns a **generator object** when called. The body doesn't execute immediately — it runs only when you iterate.

```python
def squares(n):
    for i in range(n):
        yield i ** 2

gen = squares(5)    # No code runs yet!
print(type(gen))    # <class 'generator'>

for val in gen:
    print(val)      # 0, 1, 4, 9, 16
```

### 🔄 `yield from` — Delegating to Sub-Generators

```python
def inner():
    yield 'a'
    yield 'b'

def outer():
    yield 1
    yield from inner()   # Delegate to inner generator
    yield 2

list(outer())   # [1, 'a', 'b', 2]
```

> 💡 **Tip:** `yield from` is perfect for **chaining generators** or **flattening nested structures**.

---

## 🧩 Generator Expressions

Generator expressions are like **list comprehensions**, but with `()` instead of `[]`. They are **lazy** — values are computed on demand, not all at once.

```python
# List comprehension — creates full list in memory 😬
squares_list = [x**2 for x in range(1000000)]

# Generator expression — creates nothing upfront 😎
squares_gen = (x**2 for x in range(1000000))

print(type(squares_list))   # <class 'list'>
print(type(squares_gen))    # <class 'generator'>
```

### 🔗 Chaining Generator Expressions

```python
numbers = range(20)
evens   = (x for x in numbers if x % 2 == 0)
squared = (x**2 for x in evens)

list(squared)   # [0, 4, 16, 36, 64, ...]
```

> 💡 **Tip:** When passing a generator expression as the **only argument** to a function, you can drop the extra `()`:
> ```python
> sum(x**2 for x in range(10))   # ✅ Clean!
> sum((x**2 for x in range(10))) # ✅ Also valid but redundant
> ```

---

## ⏭️ The `next()` Function

`next()` manually advances a generator to the next `yield`. When no more values remain, it raises `StopIteration`.

```python
gen = (x for x in [10, 20, 30])

print(next(gen))   # 10
print(next(gen))   # 20
print(next(gen))   # 30
print(next(gen))   # 💥 StopIteration!
```

### 🛡️ Safe `next()` with a Default

```python
gen = (x for x in [])

result = next(gen, "No more values!")
print(result)   # No more values!  ← No crash!
```

> 💡 **Tip:** Always use `next(gen, default)` when you're **not sure** if the generator is exhausted.

---

## 💾 Memory Efficiency

This is the **#1 superpower** of generators. A list stores all elements in memory at once. A generator stores **only the current state** — it uses O(1) memory regardless of size.

```python
import sys

# List — loads everything into RAM
big_list = [x for x in range(1_000_000)]
print(sys.getsizeof(big_list))   # ~8 MB 😬

# Generator — almost no memory used
big_gen = (x for x in range(1_000_000))
print(sys.getsizeof(big_gen))    # ~112 bytes 🤯
```

### 📂 Real-World Use Case — Reading Huge Files

```python
# ❌ Bad — loads entire file into RAM
def read_bad(filepath):
    return open(filepath).readlines()

# ✅ Good — reads one line at a time
def read_good(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

for line in read_good("bigfile.csv"):
    process(line)
```

---

## 🛠️ Useful Methods on Generator Objects

| Method | Description |
|---|---|
| `next(gen)` | Get the next value |
| `gen.send(val)` | Send a value **into** the generator |
| `gen.throw(exc)` | Throw an exception inside the generator |
| `gen.close()` | Stop the generator, triggers `GeneratorExit` |

### 📬 `send()` — Two-Way Communication

```python
def accumulator():
    total = 0
    while True:
        value = yield total   # Receives sent value
        total += value

gen = accumulator()
next(gen)           # Prime the generator first!
gen.send(10)        # total = 10
gen.send(20)        # total = 30
gen.send(5)         # total = 35
```

> 💡 **Tip:** Always call `next(gen)` once to **prime** a generator before using `.send()`.

---

## 🔧 Built-in Functions That Work With Generators

```python
gen = (x for x in range(10))

sum(gen)                          # Sum all values
list(gen)                         # Convert to list
tuple(gen)                        # Convert to tuple
min(gen) / max(gen)               # Min / Max value
any(x > 5 for x in range(10))    # True if any match
all(x > 0 for x in range(1, 10)) # True if all match
```

---

## 🔗 `itertools` — Generator Superpowers

```python
import itertools

itertools.chain(gen1, gen2)              # Chain multiple generators
itertools.count(start=0, step=1)         # Infinite counter
itertools.repeat(42, times=5)            # Repeat a value
itertools.islice(gen, 5)                 # Take first N items
itertools.zip_longest(gen1, gen2, fillvalue=None)  # Zip two generators
```

---

## 🧠 Quick Mental Model

```
Normal Function  →  Computes → Returns everything → Done
Generator        →  Pauses  → Yields one thing   → Resumes → Pauses → ...
```

> Generators are Python's way of saying: **"I'll give you what you need, when you need it."** 🎯

---

## 📝 Practice Questions

| # | Level | Question |
|---|---|---|
| Q1 | 🟢 Basic | Write a generator function `even_numbers(n)` that yields all even numbers from `0` to `n` |
| Q2 | 🟢 Basic | Write a generator expression that yields **cubes** of numbers `1–10` and print each using `next()` |
| Q3 | 🟡 Intermediate | Write a generator function `fibonacci()` for an infinite sequence, print first 10 using `islice()` |
| Q4 | 🟡 Intermediate | Write `read_large_file(filepath)` that yields lines one by one. Why better than `readlines()`? |
| Q5 | 🔴 Advanced | Chain three generator expressions: generate 1–20 → filter odd → square each. Print as list |

---

## 🧠 What I Learned

- 🌱 **What Generators are** — lazy iterators that produce values one at a time instead of all at once
- ⚡ **The `yield` keyword** — how it pauses a function, saves its state, and resumes from where it left off
- 🆚 **`yield` vs `return`** — yield pauses, return exits. yield remembers state, return does not
- 🏭 **Generator Functions** — functions that use `yield` and return a generator object when called
- 🔗 **`yield from`** — how to delegate to sub-generators and chain them cleanly
- 🧩 **Generator Expressions** — lazy version of list comprehensions using `()` instead of `[]`
- ⏭️ **`next()` function** — how to manually advance a generator and use a default to avoid crashes
- 💾 **Memory Efficiency** — generators use ~112 bytes vs millions of bytes for a list of the same size
- 📬 **`.send()` method** — how to pass values back into a running generator for two-way communication
- 🛡️ **`.throw()` and `.close()`** — how to handle errors and stop a generator safely
- 🔧 **Built-ins with Generators** — `sum()`, `min()`, `max()`, `any()`, `all()` all work seamlessly
- 🔗 **`itertools` module** — powerful tools like `chain()`, `islice()`, `count()`, `repeat()` to supercharge generators

---

## 🏆 Key Takeaways

- 🎯 **Generators are Lazy** — they compute values **only when asked**, not all at once upfront
- 💾 **Memory is the Superpower** — a generator of 1 million items uses the same memory as a generator of 1 item
- 🔁 **Single-Use Only** — once a generator is exhausted, it's **done**. Create a new one to reuse
- ⚡ **`yield` is the Core** — without `yield`, there is no generator. It is what makes everything work
- 🧩 **Expressions over Lists** — prefer `(x for x in ...)` over `[x for x in ...]` when you don't need all values at once
- 🔗 **Generators are Pipelines** — you can **chain** multiple generators together to build clean, efficient data pipelines
- 📂 **Best for Large Data** — reading big files, database rows, API results — generators are the **right tool**
- 🔧 **Works with Everything** — `for` loops, `sum()`, `any()`, `all()`, `itertools` — generators plug in everywhere
- 🤝 **Two-Way with `.send()`** — generators are not just output machines, you can **talk back** to them too
- 🧠 **Think Lazy, Not Eager** — the golden rule of generators is **don't produce what you don't need yet**

---

> 💬 **One Line to Remember:**
> *"Generators don't store data — they know how to produce it."* 🚀