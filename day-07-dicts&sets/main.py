# ============================================
# 🐍 Day 07 - Dictionaries & Sets
# 📅 Date: 17/04/2026
# 🎯 Goal: Understand how to store & organize data using Dictionaries and Sets — and know when to use which one.
# =============================================

# --- code starts from here ---

# dictionaries

capitals = {
    "USA": "Washington D.C.",
    "China": "Beijing",
    "Germany": "Berlin"
}

print(capitals)
print(capitals.get("USA"))

# methods of dictionaries

user = {"id": 1,
        "age": 30,
        "city": "berlin"}

# access
print(user["city"])
print(user.get("age"))

# checks
print("age" in user)
print("name" not in user)

# view objects
print(user.keys())
print(user.values())

# looping
for key, value in user.items():
    print(key, value)

# add
user["name"] = "John"
print(user)

# update
user["age"] = 35
user.update({"age": 45, "city": "Paris"})
print(user)

# remove
age = user.pop("age", "Not Found")
print(user)
print("Removed Item:", age)

# remove the last item
user.popitem()
print()

# fromkeys()
users = {
    "id": None,
    "name": None,
    "age": None,
    "city": None,
}

user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)


# dict Comprehensions
user = {"id": 1,
        "name": "John",
        "age": 30,
        "city": "berlin"}

user_str = {
    key: value.upper()  # Expression
    for key, value in user.items()  # loop
    if isinstance(value, str)  # filter
}

print(user_str)

# sets
my_set = {10, 40, 30, 20}
print(my_set)  # Unordered

# add()
my_set.add(15)
print(my_set)

# update()
my_set.update({70, 85})
print(my_set)

# |=
my_set |= {25, 35}
print(my_set)

# remove()
my_set.remove(10)
my_set.discard(10)

print(my_set)

# set math methods
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# union()
print(a.union(b))
print(a | b)

# intersection()
print(a.intersection(b))
print(a & b)

# difference()
print(a.difference(b))
print(a - b)
print(b - a)

# symmetric_difference()
print(a.symmetric_difference(b))
print(a ^ b)

# issubset() , issuperset(), isdisjoint()
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))
