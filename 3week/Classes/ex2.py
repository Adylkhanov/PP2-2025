class Shape:

    def __init__(self):
        self.i = 0

    def Area(self):
        print(self.i)

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.i = length*length


##creates a object of parent classes
a1 = Shape()
a1.Area()
##creates a object of child classes
a2 = Square(5)
a2.Area()






