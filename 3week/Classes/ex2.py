class Shape:

    def __init__(self):
        self.i = 0

    def area(self):
        print(self.i)

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.i = length*length



a1 = Shape()
a1.area()

a2 = Square(5)
a2.area()






