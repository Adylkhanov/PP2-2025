def even_numb(n):
    num = 0
    while num <= 0:
        if num % 2 == 0:
            yield num
        num+=1

a = int(input("insert you num plz"))

x = even_numb(a)
for even in x:
    print(even)