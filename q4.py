my_dict = {"Name":"Anurag" , "Age":19 , "Course":"CSE"}

my_dict_keys = my_dict.keys()
my_dict_value = my_dict.values()
my_dict_items = my_dict.items()

print("Before Modification: ")
print("Keys: ",my_dict_keys)
print("Values: ",my_dict_value)
print("Items: ",my_dict_items)
print("\n")

my_dict["Marks"] = 85
my_dict["Age"] = 21

print("After Modification: ")
print("Keys: ",my_dict_keys)
print("Values: ",my_dict_value)
print("Items: ",my_dict_items)


#when we declare my_dict_keys then it does not make a seprate copy of all the keys instead
# it is a view of dict



