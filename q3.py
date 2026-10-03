my_dict = {}
my_dict["name"] = "anurag"
my_dict["age"] = 19

my_dict["course"] = "CSE"
my_dict["gender"] = "male"

my_dict.pop("age")
my_dict["college"] = "iiitp"
my_dict.pop("gender")

my_dict["age"] = 19

print(my_dict)

#since python 3.7+ there is no change in the order even if dict is unordered this thing is 
#ensured by PyDictKeysObject 



