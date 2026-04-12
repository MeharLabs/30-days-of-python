# ============================================
# 🐍 Day 02 — Conditionals
# 📅 Date: 12/04/2026
# 🎯 Goal: Learn how to make decisions in Python by using if, elif, and else statements along with comparison, logical, membership, and identity operators — so program can think, choose, and respond based on different conditions.
# ============================================

# --- code starts from here ---

# if statement
age = 18
if age >= 18:
    print("You are an adult! ✅")

# if else statement
age = 15
if age >= 18:
    print("You are an adult! ✅")
else:
    print("You are a minor! ❌")

# if elif else statement
marks = 75
if marks >= 90:
    print("Grade: A 🏆")
elif marks >= 70:
    print("Grade: B 👍")
elif marks >= 50:
    print("Grade: C 😐")
else:
    print("Grade: F 😢")

# ============================================
# Comparison Operators
# Equal to ==, Not Equal to !=, Greater than >, Smaller than <, Greater than or Equal to >=, Smaller than or Equal to <=

x = 5

print(x == 5)  # true
print(x != 5)  # false
print(x > 5)  # false
print(x < 5)  # false
print(x >= 5)  # true
print(x <= 5)  # true

# ============================================
# Logical Operators
# and, or, not

age = 24
has_id = True

# and Operator
if age >= 18 and has_id:
    print("Entry allowed! 🎉")

# or Operator
if age >= 18 or has_id:
    print("You are an adult! ✅")

# not Operator
if age < 18:
    print("You are a minor ❌")
elif not has_id:
    print("You need an ID ⚠️")
else:
    print("You are allowed ✅")

# ============================================
# Membership Operators
# in, not in

fruits = ["apple", "banana", "mango"]

# in Operator
if "mango" in fruits:
    print("Mango is available! 🥭")

# not in Operator
if "grape" not in fruits:
    print("No grapes here! 🍇")

# ============================================
# Identity Operators
age = None

if age is None:
    print("age has no value yet! 🚫")

# ============================================
# Nested Conditionals
# if inside another if

is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome Admin! 👑")
    else:
        print("Welcome, User! 👤")
else:
    print("Please log in first! 🔒")

# ============================================
# Ternary / Inline if (One-liner!)

age = 24

# value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"

print(status)  # Adult
