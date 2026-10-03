mylist = [20,30,50,60,70,90,100]
commonDif = mylist[1] - mylist[0]
missing = []

for i in range(min(mylist), max(mylist) + 1 , commonDif):
    if i not in mylist:
        missing.append(i)

print(missing)

