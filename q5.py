# Q5: Merging Dictionaries

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

# 1. Using update()
result1 = d1.copy()
result1.update(d2)

# 2. Using | operator
result2 = d1 | d2

# 3. Using dictionary unpacking
result3 = {**d1, **d2}

print("Original d1:", d1)
print("Original d2:", d2)

print("\nUsing update():")
print(result1)

print("\nUsing | operator:")
print(result2)

print("\nUsing dictionary unpacking:")
print(result3)