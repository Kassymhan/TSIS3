class Shape:
    def printArea(self):
        print(self.length * self.width)

class Rectangular(Shape):
    def __init__(self, a, b):
        self.length = a
        self.width = b
    
    def Area(self):
        self.area = self.length * self.width

x = Rectangular(int(input()), int(input()))
x.Area()
x.printArea()