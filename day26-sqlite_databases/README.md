## 📋 Day 26 — Quick Summary

### 🎯 Short Goal
Learn SQLite & Databases in Python - what SQLite is, how to use the sqlite3 module, performing core SQL operations like CREATE, INSERT, SELECT, UPDATE, and DELETE, and understanding how Connections and Cursors work together to interact with a database. 

### 📚 Topics Covered

What is `SQLite`, the `sqlite3` module, `Connection` & `Cursor`, `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE` operations, Basic SQL Queries

### 🔨 What I Learned

✅ **What SQLite is** — a lightweight, serverless, file-based relational database built right into Python

✅ **The `sqlite3` module** — Python's built-in library requiring zero installation to work with databases

✅ **Connection** — how to open/create a database file and bridge Python to it using `sqlite3.connect()`

✅ **Cursor** — how to use it as a tool to execute SQL queries and navigate through results

✅ **CREATE** — how to build tables with data types, constraints like PRIMARY KEY, NOT NULL, UNIQUE, and AUTOINCREMENT

✅ **INSERT** — how to add single and multiple rows safely using `?` placeholders to avoid SQL injection

✅ **SELECT** — how to read and filter data using WHERE, ORDER BY, LIMIT, and LIKE

✅ **UPDATE** — how to modify existing rows with conditions to avoid accidentally changing all data

✅ **DELETE** — how to remove specific rows or clear entire tables

✅ **Basic SQL Queries** — aggregate functions like COUNT, AVG, MAX, MIN, and GROUP BY

✅ **Row Factory** — how to access row data by column name instead of index

✅ **Transactions** — how to safely batch operations with commit and rollback for data integrity

✅ **In-Memory Database** — using `":memory:"` for fast temporary databases great for testing

✅ **Best Practices** — using `with` context managers, iterating cursors directly, and storing JSON data in SQLite


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

## ⏱️ Time Spent
~ 2.5 hrs