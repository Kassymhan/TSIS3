class Point:
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5

p1 = Point()
p1.move(0, 0)
p2 = Point()
p2.move(1, 1)

print(p1.dist(p2))
