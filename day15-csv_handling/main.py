# ============================================
# 🐍 Day 15 - CSV Handling
# 📅 Date: 29/04/2026
# 🎯 Goal: Goal is to master reading and writing CSV files in Python using csv.reader, csv.writer, DictReader, DictWriter, and Pandas read_csv.
# =============================================

# --- code starts from here ---

import csv

file = "data.csv"

with open(file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line)

# skip the first line
# next(csv_reader)

# write to a new line
with open(file, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_name.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

    for line in csv_reader:
        csv_writer.writerow(line)

# using dictionary writer
with open(file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_name.csv", "w") as new_file:

        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

    for line in csv_reader:
        csv_writer.writerow(line)

# delete

with open(file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_name.csv", "w") as new_file:

        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

    for line in csv_reader:
        del line['email']
        csv_writer.writerow(line)

# pandas read_csv (basics)
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print(df.head())   # first 5 rows
print(df.tail(10))   # last 10 rows
print(df.shape)    # rows, columns
print(df.columns)  # column names


