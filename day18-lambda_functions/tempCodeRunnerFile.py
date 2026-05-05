# lambda with sort() function
values = [(1, "b", "hello"), (2, "a", "world"), (3, "c", "ok")]

sorted_values = sorted(values, key=lambda x: x[1])

print(list(sorted_values))