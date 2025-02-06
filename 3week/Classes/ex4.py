import math as mt

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("0x:" + self.x + "0y:" + self.y)
    def move(self, x1, x2):
        self.x += x1
        self.y += x2
    def dist(self,a1):
        self.distancex =abs(self.x - a1.x)
        self.distancey= abs(self.y - a1.y)
        self.dia = mt.sqrt(self.distancey**2 + self.distancex**2)
        return self.dia
a1 = Points(1, 1)
a1.move(2, 2)
a2 = Points(1, 1)

print(a1.dist(a2))