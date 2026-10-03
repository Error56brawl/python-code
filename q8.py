def fun(para1 , para2):
    x = 10
    y = 20
    z = a + b   


total = fun.__code__.co_nlocals
parameters = fun.__code__.co_argcount

total_localVariables = total - parameters
print("total: ",total)
print("parameters: ",parameters)
print("local variables: ",total_localVariables)
