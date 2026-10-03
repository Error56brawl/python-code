data = {"name": "Anurag" , "age": 20 , "course": "cse" }

print("No of key-value pairs: ",end=" ")
print(len(data))

for key,value in data.items():
    print("\n Key:" , key)
    print("\n Hash Value: ", hash(key))
    print("\n Memory Address of key: ",id(key))
    print("Value:" , value)
    print("\n Memory Address of Value: ",id(value))




