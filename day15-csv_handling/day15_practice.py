# 🟡 Level 1 — Mid (thinking required 🧠)
# =======================================
# Q1. Write a Python script that creates a students.csv file with columns name, age, marks and adds 5 student records using csv.writer.

import csv
file = "students.csv"

students = [
    ["name", "age", "marks"],
    ["John", 20, 85],
    ["Emily", 22, 90],
    ["Michael", 19, 78],
    ["Sophia", 21, 88],
    ["Daniel", 23, 92],
]


with open(file, 'w', newline="") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerows(students)

# Q2. Read the students.csv file using csv.reader and print only students who scored above 70 marks.


with open(file, "r") as csv_file:
    csv_read = csv.reader(csv_file)

    next(csv_read)

    for row in csv_read:
        if int(row[2]) > 70:
            print(row)


# 🔴 Level 2 — Hard (big brain mode 💀)
# =======================================

# Q3. Rewrite Q1 using DictWriter and Q2 using DictReader — access fields by column name instead of index.
file = "students.csv"

students = [
    {"name": "John", "age": 20, "marks": 85},
    {"name": "Emily", "age": 22, "marks": 90},
    {"name": "Michael", "age": 19, "marks": 78},
    {"name": "Sophia", "age": 21, "marks": 88},
    {"name": "Daniel", "age": 23, "marks": 92}
]

with open(file, "w", newline="") as csv_file:
    fieldnames = ["name", "age", "marks"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

with open(file, "r") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        if int(row["marks"]) > 70:
            print(row)
