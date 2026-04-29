# 📊 Day 15 — CSV Handling in Python


## 🎯 Goal
Master reading, writing, and manipulating CSV files using Python's built-in `csv` module and Pandas — the two most essential tools for working with real-world data.

## 📌 Topic Covered
CSV file handling in Python — from reading and writing with `csv.reader/writer`, accessing data by name with `DictReader/DictWriter`, to powerful data analysis using Pandas `read_csv`.

---

## 📁 What is a CSV File?

**CSV (Comma-Separated Values)** is a plain text file format used to store tabular data (rows and columns), where each line is a record and each field is separated by a delimiter (usually a comma `,`).

```
name,age,city
Alice,25,Lahore
Bob,30,Karachi
```

CSV files are universally supported — Excel, Google Sheets, databases, APIs — all love CSV. 🌍

---

## 🧩 The `csv` Module

Python's built-in `csv` module lets you **read and write CSV files** without any installation.

```python
import csv  # That's it! Built-in 🎉
```

### 🔧 Key Parameters You Can Use

| Parameter | Description | Default |
|---|---|---|
| `delimiter` | Field separator | `,` |
| `quotechar` | Character to quote fields | `"` |
| `quoting` | Quoting strategy | `QUOTE_MINIMAL` |
| `skipinitialspace` | Skip space after delimiter | `False` |
| `lineterminator` | Line ending character | `\r\n` |
| `escapechar` | Escape character | `None` |

---

## 📖 `csv.reader` — Reading CSV Files

`csv.reader` reads a CSV file **row by row**, returning each row as a **list of strings**.

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)       # ⏭️ Skip header row
    print("Headers:", header)

    for row in reader:
        print(row)              # ['Alice', '25', 'Lahore']
```

### 🛠️ Useful `csv.reader` Tricks

```python
# 📌 Custom delimiter (TSV - Tab Separated)
reader = csv.reader(file, delimiter='\t')

# 📌 Handle files with spaces after commas
reader = csv.reader(file, skipinitialspace=True)

# 📌 Get row count
with open("data.csv") as f:
    row_count = sum(1 for row in csv.reader(f))
print(f"Total rows: {row_count}")

# 📌 Read into a list at once
with open("data.csv") as f:
    all_rows = list(csv.reader(f))
```

---

## ✍️ `csv.writer` — Writing CSV Files

`csv.writer` writes data **row by row** to a CSV file.

```python
import csv

data = [
    ["name", "age", "city"],       # Header
    ["Alice", 25, "Lahore"],
    ["Bob", 30, "Karachi"],
    ["Sara", 22, "Islamabad"]
]

with open("output.csv", "w", newline="") as file:  # ⚠️ newline="" is important!
    writer = csv.writer(file)
    writer.writerows(data)          # Write all rows at once ✅
```

### 🛠️ Writer Methods

```python
writer.writerow(["Alice", 25])      # ✏️ Write a single row
writer.writerows(list_of_rows)      # ✏️ Write multiple rows at once
```

```python
# 📌 Append to existing CSV (mode='a')
with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["New Person", 28, "Multan"])

# 📌 Custom delimiter
writer = csv.writer(file, delimiter='|')
# Result: Alice|25|Lahore

# 📌 Quote all fields
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
# Result: "Alice","25","Lahore"
```

### ⚠️ Why `newline=""`?
Without it, Python adds **extra blank lines** between rows on Windows. Always use `newline=""` when opening files for `csv.writer`!

---

## 📒 `DictReader` — Reading as Dictionaries

`DictReader` reads each row as an **`OrderedDict`** (or regular dict in Python 3.8+), using the **header row as keys**. Much more readable! 🎯

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["age"], row["city"])
        # Alice 25 Lahore
```

### 🔑 Each row looks like:
```python
{'name': 'Alice', 'age': '25', 'city': 'Lahore'}
```

### 🛠️ DictReader Tricks

```python
# 📌 Check available field names (column headers)
print(reader.fieldnames)    # ['name', 'age', 'city']

# 📌 Custom headers (if CSV has no header row)
reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

# 📌 Filter rows by condition
with open("data.csv") as f:
    reader = csv.DictReader(f)
    adults = [row for row in reader if int(row["age"]) >= 25]

# 📌 Convert to list of dicts instantly
with open("data.csv") as f:
    records = list(csv.DictReader(f))
```

---

## 📝 `DictWriter` — Writing from Dictionaries

`DictWriter` writes dictionaries to CSV, mapping **dict keys → column headers**.

```python
import csv

employees = [
    {"name": "Alice", "age": 25, "city": "Lahore"},
    {"name": "Bob",   "age": 30, "city": "Karachi"},
]

with open("employees.csv", "w", newline="") as file:
    fields = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()            # ✅ Write header row first!
    writer.writerows(employees)     # ✅ Write all dicts
```

### 🛠️ DictWriter Methods

```python
writer.writeheader()            # 📌 Write the header row
writer.writerow({"name": "X"}) # 📌 Write one dict
writer.writerows(list_of_dicts) # 📌 Write multiple dicts
```

```python
# 📌 Handle extra/missing keys gracefully
writer = csv.DictWriter(file, fieldnames=fields, extrasaction='ignore')
# 'ignore' → silently drops keys not in fieldnames
# 'raise'  → raises ValueError (default)

# 📌 Fill missing keys with a default
writer = csv.DictWriter(file, fieldnames=fields, restval="N/A")
```

---

## 🐼 Pandas `read_csv` — The Power Tool

`pandas.read_csv()` loads a CSV into a **DataFrame** — a powerful 2D table object. This is the go-to for **data analysis**. 🚀

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df)
#     name  age       city
# 0  Alice   25     Lahore
# 1    Bob   30    Karachi
# 2   Sara   22  Islamabad
```

### ⚙️ Most Useful `read_csv` Parameters

```python
# 📌 Basic loading
df = pd.read_csv("data.csv")

# 📌 Custom delimiter
df = pd.read_csv("data.tsv", sep='\t')

# 📌 No header? Add your own
df = pd.read_csv("data.csv", header=None, names=["name", "age", "city"])

# 📌 Use a column as the index
df = pd.read_csv("data.csv", index_col="name")

# 📌 Load only specific columns
df = pd.read_csv("data.csv", usecols=["name", "city"])

# 📌 Load only first N rows
df = pd.read_csv("data.csv", nrows=100)

# 📌 Skip rows
df = pd.read_csv("data.csv", skiprows=2)

# 📌 Handle missing values
df = pd.read_csv("data.csv", na_values=["N/A", "missing", ""])

# 📌 Parse dates automatically
df = pd.read_csv("data.csv", parse_dates=["join_date"])

# 📌 Specify data types
df = pd.read_csv("data.csv", dtype={"age": int, "name": str})

# 📌 Read in chunks (for huge files 🐘)
for chunk in pd.read_csv("bigfile.csv", chunksize=1000):
    process(chunk)
```

### 🔍 Essential DataFrame Operations After Loading

```python
df.head()           # 👀 First 5 rows
df.tail()           # 👀 Last 5 rows
df.shape            # 📐 (rows, cols)
df.info()           # 🔍 Column types + nulls
df.describe()       # 📊 Stats summary
df.columns          # 📋 Column names
df.isnull().sum()   # ❓ Count missing values

# Filtering
df[df["age"] > 25]

# Saving back to CSV
df.to_csv("result.csv", index=False)   # index=False → no row numbers
```

---

## ⚡ Quick Comparison Table

| Feature | `csv.reader` | `DictReader` | `pandas` |
|---|---|---|---|
| Output type | List | Dict | DataFrame |
| Memory | 🟢 Low | 🟢 Low | 🔴 Higher |
| Speed | 🟢 Fast | 🟢 Fast | 🟡 Medium |
| Filtering | Manual | Manual | 🟢 Built-in |
| Data analysis | ❌ | ❌ | 🟢 Powerful |
| Install needed | ❌ | ❌ | ✅ pip install |

---

## 💡 Tips & Tricks

```python
# ✅ Tip 1: Always use 'with' statement — auto-closes file
with open("file.csv") as f:
    ...

# ✅ Tip 2: Always newline="" with csv.writer on Windows
open("file.csv", "w", newline="")

# ✅ Tip 3: Use encoding for special characters (Urdu, Arabic etc.)
open("file.csv", encoding="utf-8")

# ✅ Tip 4: Sniff delimiter automatically
with open("mystery.csv") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    reader = csv.reader(f, dialect)

# ✅ Tip 5: Convert string numbers from csv.reader
rows = [[int(x) if x.isdigit() else x for x in row] for row in reader]

# ✅ Tip 6: Write pandas df → CSV without index
df.to_csv("out.csv", index=False)

# ✅ Tip 7: Read only header row fast
with open("big.csv") as f:
    headers = next(csv.reader(f))
```

---

## 🧠 When to Use What?

| Situation | Use |
|---|---|
| 🔹 Simple read/write, no dependencies | `csv.reader` / `csv.writer` |
| 🔹 Access fields by name | `DictReader` / `DictWriter` |
| 🔹 Data analysis, filtering, stats | `pandas` |
| 🔹 Huge files, low memory | `csv` module (streaming) |
| 🔹 Chunked processing of huge files | `pandas chunksize` |

---

## 📚 What I Learned

- 📁 What CSV files are and why they're widely used for storing tabular data
- 🧩 How to import and use Python's built-in `csv` module (no installation needed)
- 📖 Reading CSV files row by row using `csv.reader` (each row as a list)
- ✍️ Writing CSV files using `csv.writer` with `writerow()` and `writerows()`
- ⚠️ Why `newline=""` is important when opening files for writing
- 📒 Reading CSV as dictionaries using `DictReader` (access fields by name)
- 📝 Writing dictionaries to CSV using `DictWriter` with `writeheader()`
- 🐼 Loading CSV files into a Pandas DataFrame using `pd.read_csv()`
- 🔍 Exploring data with `.head()`, `.tail()`, `.info()`, `.describe()`
- 💾 Saving a DataFrame back to CSV using `.to_csv(index=False)`
- ⚡ When to use `csv` module vs Pandas depending on the use case
- 💡 Best practices like using `with` statement and `utf-8` encoding

---

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
