# 🗄️ Day 26 - SQLite & Databases in Python


## 🎯 Goal

Learn SQLite & Databases in Python — what SQLite is, how to use the `sqlite3` module, performing core SQL operations like CREATE, INSERT, SELECT, UPDATE, and DELETE, and understanding how Connections and Cursors work together to interact with a database.


## 📌 What is SQLite?

**SQLite** is a lightweight, serverless, self-contained relational database engine. Unlike MySQL or PostgreSQL, SQLite stores everything in a **single `.db` file** on your disk — no installation, no server, no configuration needed.

> 🧠 Think of it as a spreadsheet on steroids — but with the full power of SQL.

**Why SQLite?** 🤔

- ✅ Zero setup — works out of the box
- ✅ Portable — one file = entire database
- ✅ Built into Python's standard library
- ✅ Perfect for small-to-medium apps, prototypes, local tools
- ❌ Not ideal for high-concurrency or massive-scale production apps


## 📦 The `sqlite3` Module

Python ships with `sqlite3` built-in — **no pip install needed!**

```python
import sqlite3  # That's it! 🎉
```

The module follows **Python's DB-API 2.0 standard**, which means the same patterns work with other databases (MySQL, PostgreSQL, etc.) when you swap the library.


## 🔌 Connection & Cursor

These are the **two core objects** you'll always work with.

### 🔗 Connection

The **connection** is your bridge to the database file.

```python
import sqlite3

# Connect to a file (creates it if it doesn't exist)
conn = sqlite3.connect("school.db")

# OR: connect to an in-memory database (temporary, fast, great for testing)
conn = sqlite3.connect(":memory:")  # 💨 Lives only in RAM
```

| Method | Description |
|---|---|
| `conn.commit()` | 💾 Save (commit) changes permanently |
| `conn.rollback()` | ↩️ Undo changes since last commit |
| `conn.close()` | 🚪 Close the connection |
| `conn.execute()` | ⚡ Shortcut — run a query directly |

---

### 🖱️ Cursor

The **cursor** is your tool to execute SQL and fetch results. Think of it as a pointer that navigates through the database.

```python
cursor = conn.cursor()
```

| Method | Description |
|---|---|
| `cursor.execute(sql)` | ▶️ Run one SQL statement |
| `cursor.executemany(sql, data)` | 🔁 Run same SQL for many rows |
| `cursor.fetchone()` | 1️⃣ Fetch next single row |
| `cursor.fetchall()` | 📋 Fetch ALL remaining rows |
| `cursor.fetchmany(n)` | 🔢 Fetch next `n` rows |
| `cursor.rowcount` | 🔢 Number of rows affected |
| `cursor.lastrowid` | 🆔 ID of last inserted row |
| `cursor.description` | 📝 Column names/metadata |

---

## 🏗️ CREATE — Build Your Table

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER,
        grade   REAL,
        email   TEXT    UNIQUE
    )
""")

conn.commit()
print("✅ Table created!")
conn.close()
```

### 🧱 SQLite Data Types

| SQLite Type | Python Equivalent | Example |
|---|---|---|
| `INTEGER` | `int` | 42 |
| `REAL` | `float` | 3.14 |
| `TEXT` | `str` | "Alice" |
| `BLOB` | `bytes` | binary data |
| `NULL` | `None` | null value |

### 🔑 Constraints

```
PRIMARY KEY   → Unique identifier for each row
AUTOINCREMENT → Auto-increase ID
NOT NULL      → Field cannot be empty
UNIQUE        → No duplicates allowed
DEFAULT value → Fallback value if none provided
CHECK(cond)   → Enforce a rule (e.g. age > 0)
```


## ➕ INSERT — Add Data

### Insert One Row

```python
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# ✅ ALWAYS use ? placeholders — never f-strings (SQL injection risk!)
cursor.execute("""
    INSERT INTO students (name, age, grade, email)
    VALUES (?, ?, ?, ?)
""", ("Alice", 20, 88.5, "alice@email.com"))

conn.commit()
print(f"✅ Inserted row ID: {cursor.lastrowid}")
```

### Insert Many Rows at Once 🚀

```python
students_data = [
    ("Bob",     22, 75.0, "bob@email.com"),
    ("Charlie", 19, 91.3, "charlie@email.com"),
    ("Diana",   21, 84.7, "diana@email.com"),
]

cursor.executemany("""
    INSERT INTO students (name, age, grade, email)
    VALUES (?, ?, ?, ?)
""", students_data)

conn.commit()
print(f"✅ Inserted {cursor.rowcount} rows!")
```

> 🚨 **NEVER do this:**
> ```python
> # ❌ SQL Injection vulnerability!
> cursor.execute(f"INSERT INTO students (name) VALUES ('{name}')")
> ```


## 🔍 SELECT — Read Data

```python
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Select ALL rows
cursor.execute("SELECT * FROM students")
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)  # 👉 (1, 'Alice', 20, 88.5, 'alice@email.com')

# Select specific columns
cursor.execute("SELECT name, grade FROM students")

# fetchone() — grab a single row
cursor.execute("SELECT * FROM students WHERE id = ?", (1,))
student = cursor.fetchone()
print(student)

# fetchmany(n) — grab a limited set
cursor.execute("SELECT * FROM students")
first_two = cursor.fetchmany(2)
```

### 🔎 SELECT with Filters & Sorting

```python
# WHERE
cursor.execute("SELECT * FROM students WHERE age > ?", (19,))

# ORDER BY
cursor.execute("SELECT * FROM students ORDER BY grade DESC")

# LIMIT
cursor.execute("SELECT * FROM students LIMIT 3")

# LIKE (pattern match)
cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("A%",))

# Multiple conditions
cursor.execute("""
    SELECT name, grade
    FROM students
    WHERE age >= ? AND grade > ?
    ORDER BY grade DESC
""", (19, 80.0))

rows = cursor.fetchall()
for name, grade in rows:
    print(f"👤 {name} → {grade}")
```

### 🏷️ Get Column Names from `cursor.description`

```python
cursor.execute("SELECT * FROM students")
columns = [desc[0] for desc in cursor.description]
print(columns)  # 👉 ['id', 'name', 'age', 'grade', 'email']

# Build a list of dicts 🔥
rows = cursor.fetchall()
students = [dict(zip(columns, row)) for row in rows]
print(students[0])  # 👉 {'id': 1, 'name': 'Alice', 'age': 20, ...}
```


## ✏️ UPDATE — Modify Data

```python
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Update one field
cursor.execute("""
    UPDATE students
    SET grade = ?
    WHERE name = ?
""", (95.0, "Alice"))

conn.commit()
print(f"✅ Updated {cursor.rowcount} row(s)")

# Update multiple fields
cursor.execute("""
    UPDATE students
    SET age = ?, grade = ?
    WHERE id = ?
""", (23, 99.0, 2))

conn.commit()
```

> ⚠️ Always use `WHERE` in `UPDATE`! Without it, you'll update **every single row**.


## 🗑️ DELETE — Remove Data

```python
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Delete one row
cursor.execute("DELETE FROM students WHERE id = ?", (3,))
conn.commit()
print(f"🗑️ Deleted {cursor.rowcount} row(s)")

# Delete with condition
cursor.execute("DELETE FROM students WHERE grade < ?", (50.0,))
conn.commit()

# ☢️ Delete EVERYTHING in table (keep structure)
cursor.execute("DELETE FROM students")
conn.commit()
```


## 🔗 Basic SQL Queries Reference

```sql
-- 📊 Aggregate functions
SELECT COUNT(*)        FROM students;
SELECT AVG(grade)      FROM students;
SELECT MAX(grade)      FROM students;
SELECT MIN(age)        FROM students;
SELECT SUM(grade)      FROM students;

-- 🗂️ GROUP BY
SELECT age, COUNT(*) FROM students GROUP BY age;

-- 🔗 HAVING (filter after GROUP BY)
SELECT age, AVG(grade) FROM students
GROUP BY age HAVING AVG(grade) > 80;

-- 🔀 JOIN (two tables)
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c     ON e.course_id = c.id;

-- 📋 Check if table exists
SELECT name FROM sqlite_master
WHERE type='table' AND name='students';
```


## 🧰 Tips & Tricks

### ✅ Use Context Manager (`with`) — Auto commits & closes!

```python
import sqlite3

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())
# 🔒 Connection automatically closed here
```

### 🏎️ Row Factory — Access columns by name!

```python
conn = sqlite3.connect("school.db")
conn.row_factory = sqlite3.Row  # 🔥 Magic line

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
row = cursor.fetchone()

print(row["name"])   # 👉 Alice  (instead of row[1])
print(row["grade"])  # 👉 88.5
```

### 📦 Store Python Dicts/Lists as JSON in SQLite

```python
import json

data = {"hobbies": ["chess", "coding"], "city": "Lahore"}
cursor.execute("INSERT INTO users (name, meta) VALUES (?, ?)",
               ("Bilal", json.dumps(data)))   # 💾 Serialize

cursor.execute("SELECT meta FROM users WHERE name = 'Bilal'")
raw = cursor.fetchone()[0]
meta = json.loads(raw)   # 📤 Deserialize
print(meta["hobbies"])   # 👉 ['chess', 'coding']
```

### 🔁 Iterate Cursor Directly (memory efficient!)

```python
cursor.execute("SELECT * FROM students")
for row in cursor:           # 🔥 No fetchall() needed
    print(row)               # Loads one row at a time
```

### 🛡️ Transactions (Batch Safety)

```python
try:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name) VALUES (?)", ("Eve",))
    cursor.execute("INSERT INTO students (name) VALUES (?)", ("Frank",))
    conn.commit()    # ✅ Both saved together
    print("✅ Transaction complete")
except Exception as e:
    conn.rollback()  # ↩️ Both reverted on failure
    print(f"❌ Transaction failed: {e}")
finally:
    conn.close()
```


## 🗺️ Full Cheat Sheet Summary

```
sqlite3.connect(db)        → 🔌 Open/create database
conn.cursor()              → 🖱️ Create cursor
cursor.execute(sql, data)  → ▶️  Run one query
cursor.executemany(sql, [])→ 🔁 Run query for many rows
cursor.fetchone()          → 1️⃣ Get one row
cursor.fetchall()          → 📋 Get all rows
cursor.fetchmany(n)        → 🔢 Get n rows
cursor.lastrowid           → 🆔 Last inserted ID
cursor.rowcount            → 🔢 Rows affected
cursor.description         → 📝 Column names
conn.commit()              → 💾 Save changes
conn.rollback()            → ↩️ Undo changes
conn.close()               → 🚪 Close connection
conn.row_factory           → 🏷️ Access rows by name
":memory:"                 → 💨 Temporary in-RAM database
```


## 📚 What I Learned

- 🗄️ **What SQLite is** — a lightweight, serverless, file-based relational database built right into Python
- 📦 **The `sqlite3` module** — Python's built-in library requiring zero installation to work with databases
- 🔌 **Connection** — how to open/create a database file and bridge Python to it using `sqlite3.connect()`
- 🖱️ **Cursor** — how to use it as a tool to execute SQL queries and navigate through results
- 🏗️ **CREATE** — how to build tables with data types, constraints like PRIMARY KEY, NOT NULL, UNIQUE, and AUTOINCREMENT
- ➕ **INSERT** — how to add single and multiple rows safely using `?` placeholders to avoid SQL injection
- 🔍 **SELECT** — how to read and filter data using WHERE, ORDER BY, LIMIT, and LIKE
- ✏️ **UPDATE** — how to modify existing rows with conditions to avoid accidentally changing all data
- 🗑️ **DELETE** — how to remove specific rows or clear entire tables
- 📊 **Basic SQL Queries** — aggregate functions like COUNT, AVG, MAX, MIN, and GROUP BY
- 🏎️ **Row Factory** — how to access row data by column name instead of index
- 🛡️ **Transactions** — how to safely batch operations with commit and rollback for data integrity
- 💨 **In-Memory Database** — using `":memory:"` for fast temporary databases great for testing
- ✅ **Best Practices** — using `with` context managers, iterating cursors directly, and storing JSON data in SQLite


## 🔑 Key Takeaways

- 🧠 **SQLite = Zero Setup** — No server, no installation, just one `.db` file and you're ready to go
- 🐍 **Built into Python** — `import sqlite3` is all you need, no pip required
- 🔌 **Always need two things** — a **Connection** (bridge to DB) and a **Cursor** (tool to run queries)
- 🚨 **Never use f-strings in SQL** — always use `?` placeholders to prevent SQL injection attacks
- 💾 **Commit or it's gone** — changes are NOT saved unless you call `conn.commit()`
- ↩️ **Rollback is your safety net** — if something goes wrong, `conn.rollback()` undoes everything
- 🚪 **Always close connections** — or better, use `with` context manager to handle it automatically
- 🏷️ **Row Factory is a game changer** — `conn.row_factory = sqlite3.Row` lets you access data by column name instead of index number
- ⚠️ **WHERE clause is critical** — forgetting it in `UPDATE` or `DELETE` affects every single row in the table
- 💨 **`:memory:`** — use in-memory databases for testing so nothing gets written to disk
- 🔁 **`executemany()` over loops** — inserting multiple rows at once is cleaner and faster than looping
- 📋 **`cursor.description`** — your best friend for dynamically getting column names from any query result

---

> 💡 **Golden Rule:** Always use `?` placeholders, always `commit()` after writes, and always `close()` your connection (or use `with`)! 