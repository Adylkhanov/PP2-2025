def filter_prime(numbers):
    lict =[]

    for num in  numbers:
        primefactor = True
        for i in range(2, num):
            if num % i == 0:
                primefactor = False
                break
        if primefactor and num != 1:
            lict.append(num)




    return lict

print(filter_prime([10, 15, 3, 7, 18, 29, 1, 5]))


