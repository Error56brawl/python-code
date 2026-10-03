s = {1,2,3}
result = [set()]
for x in s:
    new_subsets = []

    for subset in result:
            new_subsets.append(subset | {x})
    
    result += new_subsets

print(result)

