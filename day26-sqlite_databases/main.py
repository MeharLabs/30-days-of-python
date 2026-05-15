# ============================================
# 🐍 Day 26 - SQLite & Databases
# 📅 Date: 15/05/2026
# 🎯 Goal: Learn SQLite & Databases in Python - what SQLite is, how to use the sqlite3 module, performing core SQL operations like CREATE, INSERT, SELECT, UPDATE, and DELETE, and understanding how Connections and Cursors work together to interact with a database. 
# =============================================

# --- code starts from here ---

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


# INSERT - add data
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# ✅ ALWAYS use ? placeholders — never f-strings (SQL injection risk!)
cursor.execute("""
    INSERT INTO students (name, age, grade, email)
    VALUES (?, ?, ?, ?)
""", ("Alice", 20, 88.5, "alice@email.com"))

conn.commit()
print(f"✅ Inserted row ID: {cursor.lastrowid}")

# SELECT - read data

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Select ALL rows
cursor.execute("SELECT * FROM students")
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)

# Select specific columns
cursor.execute("SELECT name, grade FROM students")

# fetchone() — grab a single row
cursor.execute("SELECT * FROM students WHERE id = ?", (1,))
student = cursor.fetchone()
print(student)

# fetchmany(n) — grab a limited set
cursor.execute("SELECT * FROM students")
first_two = cursor.fetchmany(2)


# UPDATE - modify data
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

# DELETE - remove data
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
