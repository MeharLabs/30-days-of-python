# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. Create a list of 5 of your favorite foods. Print the first and last item using indexing.
fav_foods = ["Fish and Chips", "English Breakfast",
             "Pizza", "Biryani", "Burger"]

print("First:", fav_foods[0])
print("Last", fav_foods[-1])


# Q2. Add "pizza" to the end of your list, then remove the second item. Print the final list.
list = ["Fish", "Chips"]
list.append("Pizza")
list.pop(1)

print(list)

# Q3. Create a tuple of 3 cities. Try to change one value — what happens? 🤔
cities = ("New York", "Los Angeles", "Toronto")

cities.pop(1)  # Error: Can't change values in Tuples


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q4. Given this list:
# nums = [5, 3, 8, 1, 9, 2, 7]
# Sort it, reverse it, and print the largest and smallest number — without using max() or min().

nums = [5, 3, 8, 1, 9, 2, 7]

nums.sort()
nums.sort(reverse=True)

smallest = nums[0]
largest = nums[-1]

print("Sorted (desc):", nums)
print("Smallest:", smallest)
print("Largest:", largest)


# Q5. Write a list comprehension that takes this list and returns only the even numbers squared:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output → [4, 16, 36, 64]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [ number ** 2 for number in numbers if number % 2 == 0 ]

print (even_numbers)

# Q6. Unpack this tuple into 4 separate variables and print each one with a label:
# pythonstudent = ("Ali", 20, "Computer Science", 3.8)

pythonstudent = ("Ali", 20, "Computer Science", 3.8)

name, age, occupation, cgpa = pythonstudent

print(f"""
      Name: {name}
      Age: {age}
      Occupation: {occupation}
      CGPA: {cgpa}
      """)



# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q7. Write a program that:

# Takes a list of numbers
# Removes all duplicates
# Sorts it in descending order
# Prints the top 3 numbers

# data = [4, 7, 2, 7, 1, 9, 4, 3, 9, 5]
# Expected output → [9, 7, 5]

data = [4, 7, 2, 7, 1, 9, 4, 3, 9, 5]

# remove duplicates
unique_data = list(set(data))

# sort descending
unique_data.sort(reverse=True)

# top 3 numbers
top_3 = unique_data[:3]

print(top_3)


# Q8. Given a list of tuples representing students and their scores, print the name of the highest scoring student:
# pythonstudents = [("Ali", 88), ("Sara", 95), ("John", 76), ("Zara", 91)]

students = [("Ali", 88), ("Sara", 95), ("John", 76), ("Zara", 91)]

highest_student = max(students, key=lambda student: student[1])
print(highest_student[0])
