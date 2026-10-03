my_dict = {i:(i**2 if i%2==0 else i**3) for i in range(1,21) if(i**2 if i%2==0 else i**3)%4==0}
print(my_dict)