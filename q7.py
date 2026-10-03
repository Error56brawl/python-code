def fun(n):
    print(0,end=" ")
    print(1,end = " ")
    first = 0
    second = 1
    for i in range(n-2):
        num = first + second
        print(num,end=" ")
        first = second
        second = num

n = int(input("Enter num: "))
fun(n)


