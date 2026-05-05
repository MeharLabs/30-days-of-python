## 📋 Day 18 — Quick Summary

### 🎯 Short Goal

Lambda functions and Map/Filter in Python, learning how to write concise anonymous functions with lambda, transform data using map(), filter data using filter(), sort smartly with sorted(key=), and know exactly when to use lambda versus a regular function.

---

### 📚 Topics Covered

Lambda syntax, map() function, filter() function, sorted() with key, and when to use lambda vs regular functions — along with related tools like reduce(), operator.itemgetter(), list comprehensions, and pro tips for chaining and combining them together. 

---

### 🔨 What I Learned


✅  **Lambda** is an anonymous one-line function using the syntax `lambda arguments: expression`

✅  **`map()`** applies a function to every item in a list and transforms it

✅  **`filter()`** keeps only the items where the function returns `True`

✅  **`sorted(key=)`** lets you sort by any custom rule using a lambda

✅  Lambda **cannot** have multiple statements, loops, or a `return` keyword

✅  **`filter(None, list)`** instantly removes all falsy values from a list

✅  **`reduce()`** from `functools` folds an entire list into a single value

✅  **`map()` + `filter()`** can be chained together for powerful one-liners

✅  Use lambda for **short, in-place, one-time logic** only

✅  Switch to **`def`** when logic is complex or needs to be reused

✅  **`operator.itemgetter()`** is a cleaner alternative to lambda for sorting dicts

✅  Lambdas work great inside **dictionaries as dispatch tables**



## 🔑 Key Takeaways

- ⚡ **Lambda = anonymous function** — no name, no `def`, just quick inline logic
- 🗺️ **`map()` = Transform** — changes every item, output size stays the same
- 🔍 **`filter()` = Select** — picks items, output size shrinks or stays same
- 🔡 **`sorted(key=)` = Custom Sort** — sort by anything using a lambda rule
- 🔗 **Chaining** `map()` + `filter()` together creates powerful one-liners
- 📏 **One expression only** — lambda can't handle complex multi-step logic
- 🧹 **`filter(None, list)`** is the quickest way to clean falsy values
- ⚙️ **`reduce()`** is the third musketeer alongside `map()` and `filter()`
- 🏆 **`operator.itemgetter()`** beats lambda when sorting lists of dictionaries
- 🎯 **Use lambda** when logic is short, simple, and used only once in-place
- 🚫 **Avoid lambda** when you need loops, multiple lines, or reusability
- 📖 **Readability wins** — if your lambda needs a comment, write a `def` instead


## ⏱️ Time Spent
~ 2.5 hrs