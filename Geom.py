import math


class Point(object):

    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get distance to another Point object

    def dist(self, other):

        return math.hypot(self.x - other.x, self.y - other.y)

    # String representation of a Point Coordinate
    # def __str__(self):
        # return '(' + str(self.x) + ',' + str(self.y) + ')'

    # def __eq__(self, other):
        # tol = 1.0e-6
        # return((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

def main():
    a = Point()
    b = Point(3, 4)
    c = Point (3, 4)


    print(a)
    print(b)
    print(c)

    print(a.dist(b))
    print(b.dist(a))

    if (b == c):
        print('Point objects are equal')
    else:
        print('Point objects are not equal')

main()
