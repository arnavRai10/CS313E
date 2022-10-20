
#  File: Hull.py

#  Description:

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Tejas Bansal

#  Partner UT EID: tb34442

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 9/24/22

#  Date Last Modified: 9/26/22

import sys
import math


class Point (object):

    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return False
          else:
            return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
          if (abs(self.y - other.y) < tol):
            return True
          else:
            return (self.y >= other.y)
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    return ((q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x))

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):

    # Empty 2D array for top half of convex hull
    upper_hull = []

    # loop through list of points
    for i in sorted_points:
        # While the upper_hull has more than 2 values and the determinant of the second to last point and last point are positive
        while (len(upper_hull) >= 2) and (det(upper_hull[-2], upper_hull[-1], i) >= 0):
            upper_hull.pop()
        upper_hull.append(i)

    # Empty 2D array for bottom half of convex hull
    lower_hull = []
    # reversed because it still has to be clockwise rotation
    for i in reversed(sorted_points):
        while (len(lower_hull) >= 2) and det(lower_hull[-2], lower_hull[-1], i) >= 0:
            lower_hull.pop()
        lower_hull.append(i)

    # remove last values from both
    upper_hull.pop()
    lower_hull.pop()

    # append lower_hull values to upper_hull, making upper_hull the convex_hull
    for i in lower_hull:
        upper_hull.append(i)

    convex_hull_points = upper_hull

    return convex_hull_points

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):

    det_adder = 0
    det_2 = 0

    for i in range(len(convex_poly)):

        # loop through index of hull list
        if i == len(convex_poly) - 1:
            det_2 = (convex_poly[i].x * convex_poly[0].y)
            det_2 = det_adder + det_2
            det_adder = det_2

        else:
            det_2 = (convex_poly[i].x * convex_poly[i+1].y)
            det_2 = det_adder + det_2
            det_adder = det_2


    for i in range(len(convex_poly)):

        # loop through index of hull list
        if i == len(convex_poly) - 1:
            det_2 = (convex_poly[i].y * convex_poly[0].x)
            det_2 = det_adder - det_2
        else:
            det_2 = (convex_poly[i].y * convex_poly[i+1].x)
            det_2 = det_adder - det_2
            det_adder = det_2

    area = (1/2) * abs(det_2)
    return (area)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"

def main():
# create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)

    # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        points_list.append(Point (x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)


    # print the sorted list of Point objects
    ''' for p in sorted_points:
        print (str(p))

    '''
    # get the convex hull
    hull = convex_hull(sorted_points)

    # run your test cases

    # print your results to standard output
    print('Convex Hull')
    for i in hull:
        print(i)

    # print the convex hull

    # get the area of the convex hull
    print()
    area = area_poly(hull)
    # print the area of the convex hull
    print(f'Area of Convex Hull = {area}')

if __name__ == "__main__":
    main()
