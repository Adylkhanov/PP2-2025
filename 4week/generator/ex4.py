def allsquares(a,b):
    for i in range(a, b+1):
        yield i**2


a = int(input("write your first number"))
b = int(input("write your second number"))

yep = allsquares(a, b)

for x in yep:
    print(x)

