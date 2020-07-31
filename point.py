class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_x(self):
        print(self.x)

    def print_y(self):
        print(self.y)

class Shape:
    def contains(self):
        return true

point = Point(2, 4)
point.print_x()