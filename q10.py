import sys

dict_10 = {i: i for i in range(10)}
dict_100 = {i: i for i in range(100)}
dict_1000 = {i: i for i in range(1000)}

print("Memory used by dictionary with 10 keys:", sys.getsizeof(dict_10), "bytes")
print("Memory used by dictionary with 100 keys:", sys.getsizeof(dict_100), "bytes")
print("Memory used by dictionary with 1000 keys:", sys.getsizeof(dict_1000), "bytes")