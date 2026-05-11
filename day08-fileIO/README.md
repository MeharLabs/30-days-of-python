## 📋 Day 8 — Quick Summary

### 🎯 Short Goal
Understand Python File I/O — learning how to read from and write to files, exploring different file modes, methods, and modules like `os`, `json`, `csv`, and `pathlib`.

---

### 📚 Topics Covered
Python File I/O — reading, writing, and appending files, file modes, file methods, and working with os, json, csv, and pathlib modules.

---

### 🔨 What I Learned / Built

✅  What File I/O is and why it's used
✅  The open() function and all its file modes (r, w, a, rb, x etc.)
✅  Writing to files using .write() and .writelines()
✅  Reading files using .read(), .readline(), and .readlines()
✅  The with statement as the best practice for file handling
✅  Looping through a file line by line
✅  All important file methods like .seek(), .tell(), .flush(), .truncate() etc.
✅  Working with the os module for file management
✅  Reading and writing JSON files using json.dump() and json.load()
✅  Reading and writing CSV files using the csv module
✅  Handling binary files like images
✅  Common errors and fixes in File I/O
✅  Tips & Tricks like encoding, seek(0), checking file existence etc.


## 🔑 Key Takeaways

🔑 Always use with open() — it automatically closes the file and prevents data loss
⚠️ Know your modes — using the wrong mode like "w" instead of "a" can wipe your entire file
💾 File I/O makes data persist — data survives after the program ends, unlike variables
🧩 JSON is for structured data — best for saving dictionaries, lists, and nested data
📊 CSV is for tabular data — best for rows and columns like spreadsheets
🔤 Always specify encoding="utf-8" — especially when dealing with non-English or special characters
📍 seek(0) resets the cursor — you can re-read a file without closing and reopening it
🆕 pathlib is the modern approach — cleaner and more powerful than traditional open() for file management
🗂️ os module manages files and folders — rename, delete, check existence without leaving Python
🐍 File I/O is a core real-world skill — used in almost every project like apps, bots, data tools, and automation


## ⏱️ Time Spent
~ 3 hrs