# ============================================
# 🐍 Day 03 — Loops
# 📅 Date: 13/04/2026
# 🎯 Goal:
# ============================================

# --- code starts from here ---

# for loop
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in numbers:
    print(f"Number: {number}")


items = "Python"
for item in items:
    print(f"Character: {item}")


fruits = ["Apple", "Banana", "Grapes", "Oranges"]
for fruit in fruits:
    print(fruit)

# range()
for item in range(5):
    print(f"Number: {item}")

for item in range(1, 10):
    print(f"Number: {item}")

for item in range(1, 10, 2):
    print(f"Odd Number: {item}")


scores = [40, 80, 50, 42]
total = 0
for score in scores:
    total += score
    print(f"Total: {total}")
print(f"Final Total: {total}")


files = ["Report.csv", "DATA.csv", "final.TXT"]
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")

# break statement: Stops the loop immediately
for item in range(10):
    if item == 7:
        break
    print(item)

names = ["John", "Ema", "", "Patrick"]
for name in names:
    if name == "":
        break
    print(f"Name = {name}")

# continue statement: Skips the current iteration
for item in range(10):
    if item == 2:
        continue
    print(item)

names = ["John", "Ema", "", "Patrick"]
for name in names:
    if name == "":
        continue
    print(f"Name = {name}")

# pass statement: Means do nothing
names = ["John", "Ema", "", "Patrick"]
for name in names:
    if name == "":
        pass
    print(f"Name = {name}")

# else in loop
numbers = [1, 2, 3, 5, 7, 9]
for number in numbers:
    print(number)
else:
    print("Loop is completed")

# else + break in loop: Always use else with break statement
numbers = [1, 2, 3, 5, 7, 9]
for number in numbers:
    if number % 2 == 0:
        print(f"Even number: {number}")
        break
else:
    print(f"All numbers are odd")

# enumerate(): Get index + Value at the same time
names = ["John", "Sarah", "Ema"]

for index, name in enumerate(names):
    print(index, name)
# 0 John
# 1 Sarah
# 2 Ema

# zip(): Loop through two lists at once
names = ["Ali", "Sara"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, "scored", score)

# loop through a dictionary
student = {"name": "Sarah", "age": 20}

for key, value in student.items():
    print(key, ":", value)


# nested loops
for i in range(3):  # outer loop
    for j in range(2):  # inner loop
        print(f"({i}, {j})")


years = [2025, 2026]
months = ["March", "April", "May"]
days = range(1, 31)

for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}_{month}_{day}.csv")

# while loops
# while True:
# print("I will never stop!")  # 💀 Don't run this without a break!


# while true
while True:
    answer = input("Type 'quit' to stop: ").strip().lower()
    if answer == "quit":
        break  # ✅ Safe exit
