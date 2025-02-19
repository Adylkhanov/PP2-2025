def square(N):
    k = 1
    i = 1
    while k <= N:
        i = i*i

        print(i)
        k += 1
        i = k

x = int(input("Insert your number"))

square(x)