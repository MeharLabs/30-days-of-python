# ============================================
# 🐍 Day 08 - File I/O
# 📅 Date: 20/04/2026
# 🎯 Goal: Goal is to understand Python File I/O — learning how to read from and write to files, exploring different file modes, methods, and modules like os, json, and csv
# =============================================

# --- code starts from here ---

# METHOD 1: The open() Function

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

# =============================================

# Reading a file 

file = open("notes.txt", "r")

# Method 1: read() — reads ENTIRE file as one string
content = file.read()
print(content)

# Method 2: readline() — reads ONE line at a time
line = file.readline()

# Method 3: readlines() — reads ALL lines into a LIST
lines = file.readlines()  # ['Line 1\n', 'Line 2\n', ...]

file.close()

# =============================================

# METHOD 2: The with Statement 

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

# Most memory-efficient way to read large files 💡
with open("bigfile.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes \n

