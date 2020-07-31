class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Shape:
    def contains(self):
        return true

point = Point(2, 4)
print(point.get_x())