# 🟢 Level 1 — Easy (just getting started)
# =======================================
# 1. Create a dictionary with 3 friends and their ages. Print only the names (keys).
friends = {
    "Ali": 22,
    "Sara": 21,
    "John": 23
}

print(friends.keys())


# 2. Add a new key "city" to an existing dictionary and print the updated dict.
friends = {
    "Ali": 22,
    "Sara": 21,
    "John": 23
}

friends["City"] = "NYC"
print(friends)

# 3. Create a set of 5 numbers with 2 duplicates — prove duplicates are removed.

numbers = [1, 2, 3, 5, 4, 5, 1]
unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique list:", unique_numbers)

# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# 4. Check if a key "email" exists in a dictionary and print "Found" or "Not Found".
persona = {
    "name": "John",
    "email": "John@gmail.com"
}

if "email" in persona:
  print("Found")
else:
  print("Not Found")

# 5. Convert this list to a set to remove duplicates:
# items = ["pen", "book", "pen", "ruler", "book", "pen"]

items = ["pen", "book", "pen", "ruler", "book", "pen"]
remove_duplicates = list(set(items))

print(remove_duplicates)



# 6. Write a program that counts how many times each word appears in a sentence using a dictionary.
# sentence = "the cat sat on the mat the cat"

sentence = "the cat sat on the mat the cat"

words = sentence.split()
word_count = {}

for word in words:
  if word in word_count:
    word_count[word] +=1
  else:
    word_count[word] =1

print(word_count)


# 7. Given two sets, find:
# ✅ Common elements
# ➕ All elements combined
# ➖ Elements only in the first set
# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("Common Elements:", a.intersection(b))
print("All Elements Combined:", a.union(b))
print("Elements only in first set:", a.difference(b))


# 8. Merge two dictionaries into one:
# d1 = {"name": "Ali", "age": 20}
# d2 = {"city": "Lahore", "grade": "A"}

d1 = {"name": "Ali", "age": 20}
d2 = {"city": "Lahore", "grade": "A"}

print(d1 | d2)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# 9. Invert a dictionary (swap keys and values):
# original = {"a": 1, "b": 2, "c": 3}
# Expected: {1: "a", 2: "b", 3: "c"}

original = {"a": 1, "b": 2, "c": 3}
inverted = {}

for key, value in original.items():
  inverted[value] = key

print(inverted)



# 10. Write a program to find duplicate characters in a string using a set.
# text = "programming"
# # Find characters that appear more than once

text = "programming"

seen = set()
duplicates = set()

for char in text:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print(duplicates)