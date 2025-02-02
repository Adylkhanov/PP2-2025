class Stringer:
    def __init__(self):
        self.str = ""

    def getstring(self):
        self.str = input()

    def Printstring(self):
        print(self.str.upper())

p1 = Stringer()
p1.getstring()
p1.Printstring()



