## 📋 Day 15 — Quick Summary

### 🎯 Short Goal
Goal is to master reading and writing CSV files in Python using csv.reader, csv.writer, DictReader, DictWriter, and Pandas read_csv.

---

### 📚 Topics Covered
CSV file handling in Python - from reading and writing with `csv.reader/writer`, accessing data by name with `DictReader/DictWriter`, to powerful data analysis using Pandas `read_csv`.

---

### 🔨 What I Learned

 
✅ What CSV files are and why they're widely used for storing tabular data

✅ How to import and use Python's built-in `csv` module (no installation needed)

✅ Reading CSV files row by row using `csv.reader` (each row as a list)

✅ Writing CSV files using `csv.writer` with `writerow()` and `writerows()`

✅ Why `newline=""` is important when opening files for writing

✅ Reading CSV as dictionaries using `DictReader` (access fields by name)

✅ Writing dictionaries to CSV using `DictWriter` with `writeheader()`

✅ Loading CSV files into a Pandas DataFrame using `pd.read_csv()`

✅ Exploring data with `.head()`, `.tail()`, `.info()`, `.describe()`

✅ Saving a DataFrame back to CSV using `.to_csv(index=False)`

✅When to use `csv` module vs Pandas depending on the use case

✅ Best practices like using `with` statement and `utf-8` encoding




## 🔑 Key Takeaways

- 🐍 **`csv` module is built-in** — no installation, lightweight, and perfect for simple read/write tasks
- 🎯 **Use `DictReader/DictWriter`** when you want to access data by column name instead of index — cleaner and more readable
- 🐼 **Pandas is the powerhouse** — use it when you need to filter, analyze, or transform data, not just read/write
- ⚠️ **Always use `newline=""`** when writing CSV on Windows to avoid extra blank lines
- 🔒 **Always use `with` statement** to open files — it auto-closes and prevents file corruption
- 🌍 **Always specify `encoding="utf-8"`** when dealing with special or non-English characters
- 📊 **`csv` module streams row by row** — memory efficient for large files, unlike Pandas which loads everything at once
- 💾 **Always use `index=False`** in `.to_csv()` to avoid saving unwanted row numbers
- 🧠 **Right tool for the right job** — `csv` for lightweight tasks, `DictReader/Writer` for named access, `Pandas` for data analysis



## ⏱️ Time Spent
~ 2.5 hrs