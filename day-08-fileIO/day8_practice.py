# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Create a program that asks the user to enter their name and age, then saves this information to a file called profile.txt. After saving, read the file and print its contents.

user_name = input("What is your name: ")
user_age = input("What is your age: ")

with open("profile.txt", "a") as file:
    file.write(f"name: {user_name}, age: {user_age}")

with open("profile.txt", "r") as file:
    content = file.read()
    print(content)


# Q2. Write a program that writes the numbers 1 to 10 (each on a new line) into a file called numbers.txt. Then read the file and print only the even numbers.

with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip())   # remove \n and convert to int
        if num % 2 == 0:
            print(num)

# Q3. You have a file notes.txt. Write a program that appends a new line "Python is fun! 🐍" to it every time it runs, without deleting the old content. Then print how many lines the file has in total.

file_name = "notes.txt"

with open(file_name, "a") as file:
    file.write("Python is fun! 🐍\n")

with open(file_name, "r")as file:
    lines = file.readlines()
    print("Total lines:", len(lines))


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q4. Write a program that reads a text file and counts:

# Total number of lines
# Total number of words
# Total number of characters

# (You can create your own text file with a few sentences to test it)

file_name = "notes.txt"

with open(file_name, "r") as file:
    content = file.read()

    lines = content.split("\n")
    line_count = len(lines)

    words = content.split()
    word_count = len(words)

    char = len(content)


print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char}")


# Q5. Create a student records program that:

# Saves student name & grade to a students.csv file
# Lets the user add as many students as they want (loop until they type "done")
# At the end, reads the CSV and prints all records neatly

file_name = "students_record.csv"

with open(file_name, "a") as file:
    
    while True:
        name = input("Enter your name (or type 'done' to stop): ")
        if name.lower() == "done":
            break
        grade = input("Enter your grade: ")  
        file.write(f"{name},{grade}\n")


# 🔴 Level 3 — Hard (big brain mode 💀)
# ======================================= 
    
# Q6. Write a program that reads a file and creates a copy of it with the word "copy_" added to the filename. For example, notes.txt → copy_notes.txt

file_name = "students_record.csv"
copy_file = "copy_" + file_name

with open(file_name, "r") as file:
    data = file.read()

with open(copy_file, "w") as target:
    target.write(data)

print(f"File copied to {copy_file}")

# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================
