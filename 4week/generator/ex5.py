def pain(n):
    while n >=0:
        yield n
        n -=1


n = int(input())
a = pain(n)

for elements in a:
    print(elements)