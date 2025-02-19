import math

def polyarea(r, n):

    return round((n*r*r)/4*math.tan(math.pi/n))


numbers = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

area  = polyarea(length, numbers)

print(f"The area of the polygon is: {area}")
