class Shape:

    def __init__(self):
        self.i = 0

    def Area(self):
        print(self.i)

class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.i = length*width


a1 = Rectangle(2, 5)
a1.Area()