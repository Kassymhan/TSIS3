class Shape:
    def printArea(self):
        print(self.length ** 2)

class Square:
    def __init__(self, a):
        self.length = a
    def Area(self):
        print(self.length ** 2)
    
a = Square(int(input()))
a.Area()