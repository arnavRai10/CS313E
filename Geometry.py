#  File: Geometry.py

#  Description:

#  Student Name: Arnav Rai

#  Student UT EID: akr2673

#  Partner Name: Tejas Bansal

#  Partner UT EID: tb34442

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/16/22

#  Date Last Modified: 9/16/22

import math
import sys

class Point(object):
    # constructor with default values
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        s = f'({self.x}, {self.y}, {self.z})'
        return s

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        x_dist = (self.x - other.x)**2
        y_dist = (self.y - other.y)**2
        z_dist = (self.z - other.z)**2
        return ((x_dist + y_dist + z_dist) ** 0.5)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)


class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1):
      self.center = Point(float(x), float(y), float(z))
      self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
      return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Radius: {self.radius}'

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
      surface_area = 4 * math.pi * (math.pow(self.radius, 2))
      return surface_area

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
      vol = math.pi * (math.pow(self.radius, 3)) * (4/3)
      return vol

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        dist = p.distance(self.center)
        return (self.radius > dist)

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        sphere_dist = self.center.distance(other.center)
        return (self.radius > (other.radius + sphere_dist))


    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        dist = self.center.distance(a_cube.center)
        hypot_half = (((a_cube.side**2) + (a_cube.side**2))**0.5)/2
        return (self.radius >= dist + hypot_half)

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        return (a_cyl.height < self.radius and a_cyl.radius < self.radius)

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        dist = abs(self.center.distance(other.center))
        if (dist < (self.radius + other.radius)):
            return True
        return False

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):

        if (a_cube.is_inside_sphere(self) == False) and (self.is_inside_cube(a_cube) == False):

            dist = abs(self.center.distance(a_cube.center))
            if ((a_cube.side) * 0.5) + self.radius > dist:
                return True
        return False

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):

        circum_cube = Cube(self.center.x, self.center.y, self.center.z, (2*self.radius) / math.sqrt(3))
        return circum_cube


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0, side = 1.0):
        self.center = Point(float(x), float(y), float(z))
        self.side = float(side)

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Side: {self.side}'

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):

        surface_area = 6 * math.pow(self.side, 2)
        return surface_area

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        vol = math.pow(self.side, 3)
        return vol

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        dist = p.distance(self.center)
        return (dist < (self.side/2))

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        dist = self.center.distance(a_sphere.center)
        return ((self.side/2) > dist + a_sphere.radius)

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        dist = self.center.distance(other.center)
        return (dist + other.side < self.side)

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        return (a_cyl.height < self.side)

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        dist = self.center.distance(other.center)
        if dist < (self.side + other.side) * 0.5:
            return True

        return False

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        if Cube.does_intersect_cube(self, other) is True:
            vol_dif = self.volume() - other.volume()
            return vol_dif
        else:
            vol_dif = 0
            return vol_dif


    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        inscribed_sphere = Sphere(self.center.x, self.center.y, self.center.z , (self.side/2))
        return inscribed_sphere


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1, height = 1):
        self.center = Point(float(x), float(y), float(z))
        self.radius = float(radius)
        self.height = float(height)

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Radius: {self.radius}, Height: {self.height}'

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        surface_area = (2 * math.pi * self.radius * self.height) + (2 * math.pi * math.pow(self.radius, 2))
        return surface_area

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        vol = math.pi * math.pow(self.radius, 2) * self.height
        return vol

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        if abs(p.x - self.center.x) >= self.radius:
            return False
        if abs(p.y - self.center.y) >= self.radius:
            return False
        if abs(p.z - self.center.z) >= self.height*.5:
            return False
        return True

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        if abs(self.center.x - a_sphere.center.x - a_sphere.radius) >= self.radius:
            return False
        if abs((self.center.y - a_sphere.center.y - a_sphere.radius)) >= self.radius:
            return False
        if abs(self.center.z - a_sphere.center.z - a_sphere.radius) >= self.height*.5:
            return False
        return True

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        if abs(self.center.x - a_cube.center.x - a_cube.side*.5) > self.radius:
              return False
        if abs((self.center.y - a_cube.center.y - a_cube.side*.5)) > self.radius:
            return False
        if abs(self.center.z - a_cube.center.z - a_cube.side*.5) > self.height*.5:
            return False
        return True

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        if abs(self.center.x - other.center.x - other.radius) >= self.radius:
            return False
        if abs((self.center.y - other.center.y - other.radius)) >= self.radius:
            return False
        if abs(self.center.z - other.center.z - other.height*.5) >= self.height*.5:
            return False
        return True


    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean

    def does_intersect_cylinder (self, other):

        if (self.is_inside_cylinder(other) == False):

            x2 = (self.center.x - other.center.x) * (self.center.x - other.center.x)
            y2 = (self.center.y - other.center.y) * (self.center.y - other.center.y)
            if((x2 + y2) ** 0.5) < (self.radius + other.radius):
                if abs(self.center.z - other.center.z) <= (self.height*.5+other.height*.5):
                    return True

        return False

def main():
    # read data from standard input

    # read the coordinates of the first Point p
    p_coord = sys.stdin.readline()
    p_coord = p_coord.strip()
    p_coord = p_coord.split(' ')

    p_list = []
    for i in range(3):
        # print(p_coord)
        if (p_coord[i] != ""):
            p_list.append(float(p_coord[i]))

    # create a Point object
    pointP = Point(p_list[0], p_list[1], p_list[2])

    # read the coordinates of the second Point q
    q_coord = sys.stdin.readline()
    q_coord = q_coord.strip()
    q_coord = q_coord.split(' ')

    q_list = []
    for i in range (3):
        if (q_coord[i] != ""):
            q_list.append(float(q_coord[i]))


    # create a Point object
    pointQ = Point(q_list[0], q_list[1], q_list[2])

    # read the coordinates of the center and radius of sphereA
    spA_coord = sys.stdin.readline()
    spA_coord = spA_coord.strip()
    spA_coord = spA_coord.split(' ')

    spA_list = []
    for i in range (4):
        if spA_coord[i] != "":
            spA_list.append(float(spA_coord[i]))

    # create a Sphere object
    sphereA = Sphere(spA_list[0], spA_list[1], spA_list[2], spA_list[3])

    # read the coordinates of the center and radius of sphereB
    spB_coord = sys.stdin.readline()
    spB_coord = spB_coord.strip()
    spB_coord = spB_coord.split(' ')

    spB_list = []
    for i in range (4):
        if spB_coord[i] != "":
            spB_list.append(float(spB_coord[i]))

    # create a Sphere object
    sphereB = Sphere(spB_list[0], spB_list[1], spB_list[2], spB_list[3])

    # read the coordinates of the center and side of cubeA
    cbA_coord = sys.stdin.readline()
    cbA_coord = cbA_coord.strip()
    cbA_coord = cbA_coord.split(' ')

    cbA_list = []
    for i in range (4):
        if cbA_coord[i] != "":
            cbA_list.append(float(cbA_coord[i]))

    # create a Cube object
    cubeA = Cube(cbA_list[0], cbA_list[1], cbA_list[2], cbA_list[3])

    # read the coordinates of the center and side of cubeB
    cbB_coord = sys.stdin.readline()
    cbB_coord = cbB_coord.strip()
    cbB_coord = cbB_coord.split(' ')

    cbB_list = []
    for i in range (4):
        if cbB_coord[i] != "":
            cbB_list.append(float(cbB_coord[i]))

    # create a Cube object
    cubeB = Cube(cbB_list[0], cbB_list[1], cbB_list[2], cbB_list[3])

    # read the coordinates of the center, radius and height of cylA
    cylA_coord = sys.stdin.readline()
    cylA_coord = cylA_coord.strip()
    cylA_coord = cylA_coord.split(' ')

    cylA_list = []
    for i in range (5):
        if cylA_coord[i] != "":
            cylA_list.append(float(cylA_coord[i]))

    # create a Cylinder object
    cylA = Cylinder(cylA_list[0], cylA_list[1], cylA_list[2], cylA_list[3], cylA_list[4])

    # read the coordinates of the center, radius and height of cylB
    cylB_coord = sys.stdin.readline()
    cylB_coord = cylB_coord.strip()
    cylB_coord = cylB_coord.split(' ')

    cylB_list = []
    for i in range (5):
        if cylB_coord[i] != "":
            cylB_list.append(float(cylB_coord[i]))

    # create a Cylinder object
    cylB = Cylinder(cylB_list[0], cylB_list[1], cylB_list[2], cylB_list[3], cylB_list[4])

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    p_dist = pointP.distance(Point())
    q_dist = pointQ.distance(Point())

    if p_dist > q_dist:
        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

    # print if Point p is inside sphereA
    if ((sphereA.is_inside_point(pointP)) == True):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    if ((sphereA.is_inside_sphere(sphereB)) == True):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    if ((sphereA.is_inside_cube(cubeA)) == True):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    if (cylA.is_inside_sphere(sphereA) == True):
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

    # print if sphereA intersects with sphereB
    if ((sphereB.does_intersect_sphere(sphereA)) == True):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")


    # print if cubeB intersects with sphereB
    if ((sphereB.does_intersect_cube(cubeB)) == True):
        print ("cubeB does intersect sphereB")
    else:
        print ("cubeB does not intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    circum_cube = sphereA.circumscribe_cube()
    if (circum_cube.volume() > cylA.volume()):
        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
    else:
        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')

    # print if Point p is inside cubeA
    if ((cubeA.is_inside_point(pointP)) == True):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    if ((cubeA.is_inside_sphere(sphereA)) == True):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    if ((cubeB.is_inside_cube(cubeA)) == True):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    if ((cubeA.is_inside_cylinder(cylA)) == True):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    if ((cubeA.does_intersect_cube(cubeB)) == True):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    vol_dif = cubeA.intersection_volume(cubeB)
    if vol_dif > sphereA.volume():
        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    inscribed_sphere = cubeA.inscribe_sphere()
    if inscribed_sphere.area() > cylA.area():
        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
    else:
        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')


    # print if Point p is inside cylA
    if ((cylA.is_inside_point(pointP)) == True):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    if ((cylA.is_inside_sphere(sphereA)) == True):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    if ((cylA.is_inside_cube(cubeA)) == True):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if ((cylA.is_inside_cylinder(cylB)) == True):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if ((cylA.does_intersect_cylinder(cylB)) == True):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")

if __name__ == "__main__":
    main()
