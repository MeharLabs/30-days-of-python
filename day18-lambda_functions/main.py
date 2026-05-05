# ============================================
# 🐍 Day 18 - Lambda Functions
# 📅 Date: 04/05/2026
# 🎯 Goal: Lambda functions and Map/Filter in Python, learning how to write concise anonymous functions with lambda, transform data using map(), filter data using filter(), sort smartly with sorted(key=), and know exactly when to use lambda versus a regular function.
# =============================================

# --- code starts from here ---

# lambda structure
# lambda parameter(s): expression

# lambda functions
add = lambda x, y: x + y

result = add(2, 6)
print(result)

# lambda with map() function
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda x: x**2, my_numbers))
print(square)

# lambda with filter() function
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, my_numbers))
print(evens)

# lambda with sort() function
values = [(1, "b", "hello"), (2, "a", "world"), (3, "c", "ok")]

sorted_values = sorted(values, key=lambda x: x[1])

print(list(sorted_values))

# advanced lambda functions
from functools import reduce

numbers = [1,2,3,4,5]

# Using reduce to sum the list without initializer
sun_of_numbers = reduce(lambda acc, x: acc+x, numbers)
print(sun_of_numbers)

# Using reduce to find the maximum value
max_value = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(max_value)
