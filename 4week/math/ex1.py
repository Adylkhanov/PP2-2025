import math


def degreetorad(deg):

    p = math.pi

    return float((deg * p)/180)


i = int(input("Input degree:"))
a = str(degreetorad(i))
print("Output radian: " + a)



