# 📁 Day 8: Python File I/O (Input/Output)


## 📖 Definition

**File I/O** (Input/Output) is the process of **reading data from** and **writing data to** files on your computer's storage. Python provides built-in functions and methods to interact with files — text files, CSVs, logs, configs, and more.

💡 Think of it like this: your program opens a notebook 📓, reads or writes something, then closes it. Simple!


## 🎯 Goal

Understand Python File I/O — learning how to read from and write to files, exploring different file modes, methods, and modules like `os`, `json`, `csv`, and `pathlib`.

---

## 🔓 The `open()` Function — The Gateway

Everything starts with `open()`:

```python
file = open("filename.txt", "mode")
```

### 📋 File Modes

| Mode | Symbol | Description |
|------|--------|-------------|
| Read | `"r"` | Read only (default). Error if file doesn't exist ❌ |
| Write | `"w"` | Write only. **Creates** file or **overwrites** existing ⚠️ |
| Append | `"a"` | Adds to end of file. Creates if not exists ➕ |
| Read+Write | `"r+"` | Read and write (file must exist) |
| Binary Read | `"rb"` | Read in binary (images, PDFs, etc.) 🖼️ |
| Binary Write | `"wb"` | Write in binary |
| Exclusive Create | `"x"` | Creates file. Error if already exists 🔒 |

---

## ✍️ Writing to a File

```python
# Basic write
file = open("notes.txt", "w")
file.write("Hello, World!\n")
file.write("Python is awesome! 🐍\n")
file.close()  # ⚠️ Always close!

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("notes.txt", "w")
file.writelines(lines)
file.close()
```

---

## 📖 Reading from a File

```python
file = open("notes.txt", "r")

# Method 1: read() — reads ENTIRE file as one string
content = file.read()
print(content)

# Method 2: readline() — reads ONE line at a time
line = file.readline()

# Method 3: readlines() — reads ALL lines into a LIST
lines = file.readlines()  # ['Line 1\n', 'Line 2\n', ...]

file.close()
```

---

## ⭐ The `with` Statement — THE Best Practice

The `with` block **automatically closes** the file, even if an error occurs. Always use this! 🙌

```python
# Reading
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# File is auto-closed here ✅

# Writing
with open("notes.txt", "w") as file:
    file.write("Clean and safe! ✨")

# Appending
with open("notes.txt", "a") as file:
    file.write("\nAdded a new line!")
```


## 🧰 All File Methods & What They Do

| Method | Description | Example |
|--------|-------------|---------|
| `.read(n)` | Read entire file or `n` bytes/chars | `f.read(10)` |
| `.readline()` | Read one line | `f.readline()` |
| `.readlines()` | Read all lines → list | `f.readlines()` |
| `.write(str)` | Write a string | `f.write("hi")` |
| `.writelines(list)` | Write list of strings | `f.writelines(["a","b"])` |
| `.close()` | Close the file | `f.close()` |
| `.seek(pos)` | Move cursor to position | `f.seek(0)` |
| `.tell()` | Get current cursor position | `f.tell()` |
| `.flush()` | Force write buffer to disk | `f.flush()` |
| `.truncate(size)` | Resize file to given size | `f.truncate(0)` |
| `.readable()` | Is file readable? → bool | `f.readable()` |
| `.writable()` | Is file writable? → bool | `f.writable()` |
| `.name` | Get the file name | `f.name` |
| `.mode` | Get the file mode | `f.mode` |
| `.closed` | Is file closed? → bool | `f.closed` |

---

## 🔁 Looping Through a File

```python
# Most memory-efficient way to read large files 💡
with open("bigfile.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes \n
```

---

## 📦 Working with the `os` Module

```python
import os

os.rename("old.txt", "new.txt")   # ✏️ Rename file
os.remove("file.txt")             # 🗑️ Delete file
os.path.exists("file.txt")        # ✅ Check if file exists → True/False
os.path.getsize("file.txt")       # 📏 Get file size in bytes
os.getcwd()                       # 📍 Current working directory
os.listdir(".")                   # 📂 List all files in directory
os.mkdir("new_folder")            # 📁 Create a folder
```

---

## 🧩 Working with JSON Files

```python
import json

data = {"name": "Ali", "age": 20, "city": "Rawalpindi"}

# Write JSON 📝
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON 📖
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])  # Ali
```

---

## 📊 Working with CSV Files

```python
import csv

# Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade"])  # Header
    writer.writerow(["Ali", "A"])
    writer.writerow(["Sara", "B+"])

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 🖼️ Binary Files (Images, etc.)

```python
# Copy an image using binary mode
with open("photo.jpg", "rb") as original:
    data = original.read()

with open("photo_copy.jpg", "wb") as copy:
    copy.write(data)
print("Image copied! 🖼️")
```

---

## 💡 Tips & Tricks

**🔹 Always use `with`** — never manually call `.close()` and risk leaking file handles.

**🔹 Use `.strip()`** when reading lines to remove trailing `\n`:
```python
lines = [line.strip() for line in file.readlines()]
```

**🔹 Check before opening** to avoid crashes:
```python
if os.path.exists("data.txt"):
    with open("data.txt") as f:
        print(f.read())
```

**🔹 Use `seek(0)` to re-read a file** from the beginning without reopening:
```python
with open("file.txt", "r+") as f:
    content = f.read()
    f.seek(0)          # Go back to start
    f.write("NEW CONTENT")
```

**🔹 Encoding matters** — always specify `utf-8` for non-English text:
```python
with open("urdu.txt", "w", encoding="utf-8") as f:
    f.write("یہ اردو متن ہے 🇵🇰")
```

**🔹 `"a"` vs `"w"`** — if you don't want to destroy existing content, always use append `"a"`.

**🔹 `pathlib` is the modern way** 🆕:
```python
from pathlib import Path

p = Path("notes.txt")
p.write_text("Hello from pathlib! ✨")
print(p.read_text())
print(p.exists())   # True
print(p.suffix)     # .txt
```

---

## ⚠️ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError` | File doesn't exist in read mode | Check path or use `"w"` to create |
| `PermissionError` | No access rights | Run as admin or fix permissions |
| `UnicodeDecodeError` | Wrong encoding | Add `encoding="utf-8"` |
| Garbled text | Binary file opened as text | Use `"rb"` mode |
| File not saved | Forgot to close | Use `with` statement |

---

## 🗺️ Quick Cheat Sheet

```
open() modes:   r  w  a  r+  rb  wb  x
Read methods:   .read()  .readline()  .readlines()
Write methods:  .write()  .writelines()
Cursor:         .seek()  .tell()
Always use:     with open(...) as f:
Bonus modules:  os  json  csv  pathlib
```

---

## 📚 What I Learned Today

- 📁 What **File I/O** is and why it's used
- 🔓 The `open()` function and all its **file modes** (`r`, `w`, `a`, `rb`, `x` etc.)
- ✍️ **Writing** to files using `.write()` and `.writelines()`
- 📖 **Reading** files using `.read()`, `.readline()`, and `.readlines()`
- ⭐ The `with` statement as the **best practice** for file handling
- 🔁 **Looping** through a file line by line
- 🧰 All important **file methods** like `.seek()`, `.tell()`, `.flush()`, `.truncate()` etc.
- 📦 Working with the **`os` module** for file management
- 🧩 Reading and writing **JSON files** using `json.dump()` and `json.load()`
- 📊 Reading and writing **CSV files** using the `csv` module
- 🖼️ Handling **binary files** like images
- ⚠️ Common **errors and fixes** in File I/O
- 💡 **Tips & Tricks** like encoding, `seek(0)`, checking file existence etc.

---

## 🔑 Key Takeaways

- 🔑 **Always use `with open()`** — it automatically closes the file and prevents data loss
- ⚠️ **Know your modes** — using the wrong mode like `"w"` instead of `"a"` can wipe your entire file
- 💾 **File I/O makes data persist** — data survives after the program ends, unlike variables
- 🧩 **JSON is for structured data** — best for saving dictionaries, lists, and nested data
- 📊 **CSV is for tabular data** — best for rows and columns like spreadsheets
- 🔤 **Always specify `encoding="utf-8"`** — especially when dealing with non-English or special characters
- 📍 **`seek(0)` resets the cursor** — you can re-read a file without closing and reopening it
- 🆕 **`pathlib` is the modern approach** — cleaner and more powerful than traditional `open()` for file management
- 🗂️ **`os` module manages files and folders** — rename, delete, check existence without leaving Python
- 🐍 **File I/O is a core real-world skill** — used in almost every project like apps, bots, data tools, and automation
