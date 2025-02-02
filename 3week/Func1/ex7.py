def has_33(lict):

    for i in range(len(lict) - 1):
        if lict[i] == 3 and lict[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]) )
print(has_33([1, 3, 1, 3]) )
