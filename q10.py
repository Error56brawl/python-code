def append_item(item, item_list=[]):
    item_list.append(item)
    return item_list

print(append_item(10))
print(append_item(20))
print(append_item(30))


print("USING NONE")
def append_item(item, item_list=None):
    if item_list is None:
        item_list = []

    item_list.append(item)
    return item_list

print(append_item(10))
print(append_item(20))
print(append_item(30))