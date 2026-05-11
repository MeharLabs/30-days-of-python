# 🟢 Level 1 — Easy (just getting started)
# ============================================

# Q1. Create 3 variables — your name, age, and city. Print them using f-string.
name = "Mehar Hassan"
age = 24
city = "LA"

print(f"My name is {name} and age is {age} and I lives in {city}")

# Q2. Create a list of 5 of your favorite foods. Print the first and last item.
fav_foods = ["Pizza", "Burger", "Pasta", "Fries", "Sandwich"]

print(fav_foods[0])
print(fav_foods[-1])

# Q3. Create a dict of your profile with keys — name, age, hobby. Print your hobby.
my_profile = {
    "name": "Mehar Hassan",
    "age": 24,
    "hobby": "coding"
}

print(my_profile["hobby"])

# Q4. Check the type of these values using type():
# [42, "hello", 3.14, True, [1,2,3]]
print(type(42))
print(type("hello"))
print(type(3.14))
print(type(True))
print(type([1, 2, 3]))

# Q5. Store your birthday as a tuple (day, month, year) and print each value separately.
my_age = (1, 11, 2001)
print(my_age[0])
print(my_age[1])
print(my_age[2])


# 🟡 Level 2 — Mid (thinking required 🧠)
# ============================================

# Q6. Take a number stored as string "25" and add 5 to it. Print the result.
number = "25"
print(int(number) + 5)

# Q7. Create a list of 5 numbers. Add a new number, remove the 2nd item, then print the final list.
numbers = [1, 2, 3, 4, 5]

numbers.append(8)
numbers.remove(numbers[1])
print(numbers)

# Q8. Create a student dict with name, marks, and grade. Update the marks and add a new key passed = True.
studentA = {
    "name": "Mehar Hassan",
    "marks": 99,
    "grade": "A+"
}

studentA["marks"] = 90
studentA["passed"] = True
print(studentA)

# Q9. Concatenate your first name and last name using both + and f-string. Print both results.
first_name = "Mehar"
last_name = "Hassan"

print(first_name + last_name)
print(f"{first_name} {last_name}")

# Q10. Create a tuple of 3 cities. Try to change the 2nd city — what error do you get? 👀
cities = ("London", "Los Angeles", "Toronto")
# cities[1]="Dubai" # TypeError, we can't change the values of tuple
print(cities)


# 🔴 Level 3 — Hard (big brain mode 💀)
# ============================================

# Q11. Create a dict where keys are subject names and values are marks. Print only the subject names, then only the marks.
marks_dict = {
    "English": 92,
    "Maths": 75,
    "Physics": 53,
    "Arts": 78,
    "Computer Science": 90,
}

print(marks_dict.keys())
print(marks_dict.values())

# Q12. You have this: info = ("John", 20, "NYC"). Unpack it into 3 separate variables and print each one.
info = ("John", 20, "NYC")
name, age, city = info

print(name, age, city)
