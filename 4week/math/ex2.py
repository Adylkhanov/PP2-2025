from math import atan2


def area(a, b, h):

    return ((a+b)*h)/2


h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

c = area(a, b, h)

print("Expected Output: " + str(c))