## 📋 Day 14 — Quick Summary

### 🎯 Short Goal

Master reading, writing, and manipulating JSON data in Python. Converting between strings, dictionaries, and files using json.loads(), json.dumps(), json.load(), and json.dump(), while keeping output clean with pretty printing.

---

### 📚 Topics Covered
JSON basics, converting between strings & dicts using `loads/dumps`, reading & writing JSON files using `load/dump`, and pretty printing output.

---

### 🔨 What I Learned

✅ 

✅ JSON is a lightweight data format used to exchange data between systems

✅ `json.loads()` converts a **JSON string → Python dict**

✅ `json.dumps()` converts a **Python dict → JSON string**

✅ `json.load()` reads a **JSON file → Python dict**

✅ `json.dump()` writes a **Python dict → JSON file**

✅ `indent=4` makes JSON output clean and human-readable

✅ `sort_keys=True` sorts keys alphabetically

✅ `ensure_ascii=False` supports non-English characters

✅ Always use `with open()` to safely handle files

✅ Use `.get()` for safe key access without crashes

✅ Always wrap JSON parsing in `try/except` to catch `json.JSONDecodeError`

✅ JSON only accepts **double quotes** — single quotes will break it



## 🔑 Key Takeaways

⚡ JSON is the **backbone of APIs and data exchange** in real-world projects

⚡ `loads/dumps` → work with **strings in memory**, `load/dump` → work with **files on disk**

⚡ Always **pretty print** with `indent=4` when saving or debugging JSON files

⚡ **Never trust raw JSON input** — always wrap in `try/except` for safety

⚡ `with open()` is the **right way** to handle files — always use it

⚡ JSON and Python dicts look similar but are **not the same thing**

⚡ Mastering JSON means you can **work with any API response** confidently



## ⏱️ Time Spent
~ 1.5 hrs