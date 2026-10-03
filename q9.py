import json

data = {
    "name": "Anurag",
    "age": 20,
    "marks": [85, 90, 88],
}

print("Original dictionary:")
print(data)
json_data = json.dumps(data)

print("\nSerialized JSON:")
print(json_data)
print(type(json_data))

new_data = json.loads(json_data)

print("\nDeserialized dictionary:")
print(new_data)
print(type(new_data))

