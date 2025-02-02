def spy_game(lict):
    spy_number =[0,0,7]

    for i in lict:
        if i == spy_number[0]:
            spy_number.pop(0)
        if  not spy_number:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))