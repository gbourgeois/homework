__author__ = 'bourgeois'
from numbers import Number
from numpy import pi
import math


def square_perimeter(side):
    """
    calculate the perimeter of a square from side length.
    :@param side: side length
    :@return:perimeter of square (units of side)
    >>> square_perimeter(6)
    24
    """
    return side*4


def square_area(side):
    """
    calculate the area of a square from side length.
    :@param side: the side length
    :@return:the perimeter (same units as side length)
    >>>return square_area(6)
    36
    """
    return side*side


#calculate the perimeter and the area of rectangle#


def rectangle_perimeter(length, width):
    """
    calculate the perimeter of rectangle from sides length and width.
    :@param length:the length of rectangle.
    :@return:rectangle of perimeter( a same units as length)
    >>>return rectangle_perimeter (7, 4)
    28
    """
    return (length + width)*2


def rectangle_area(length, width):
    """
    calculate the area of a rectangle from side length.
    :param length: the side length
    :param width: the side length
    :return:the perimeter (same units as side length)
    >>>return rectangle_area(9, 5)
    28
    """
    return length*width


#calculate the perimeter and the area of triangle


def triangle_perimeter(length, side, height) -> Number:
    """
    calculate the perimeter of triangle from length, side and height.
    :param side:the length of triangle.
    :param height:the height of triangle.
    @param length:the length of triangle.
    :return:triangle of perimeter( a same units as length)
    >>>return triangle_perimeter (9,6,3)
    18
    """
    return length+side+height


def triangle_area(side, height):
    """
    calculate the area of a triangle from side length.
    :param side: the side length
    :return:the area ( units  length^2)
    >>>return triangle_area(9, 5)
    28
    """
    return (side*height)/2


# calculate the perimeter and the area of trapezium


def trapezium_perimeter(length, width, side, height) -> Number:
    """
    calculate the perimeter of trapezium from sides side and height.
    :@param side:the length of triangle.
    :@param height:the height of triangle.
    @param length:the length of triangle.
    @param width:the width of triangle.
    :@return:trapezium of perimeter( a same units as length)
    >>>return trapezium_perimeter(9,5,6,3)
    23
    """
    return length + width+side+height


def trapezium_area(length, width, height):
    """
    calculate the area of a trapezium from side length.
    :@param side: the side length
    :@param height:the height of trapezium.
    @param length:the length of trapezium.
    @param width:the width of trapezium.
    :@return:the perimeter (same units as side length^2)
    >>>return trapezium_area(9, 5,3)
   21
    """
    return ((length+width)*height)/2


# calculate the perimeter and the area of regular hexagon
def regular_hexagon_perimeter(side):
    """
    calculate the perimeter of a regular hexagon from side length.
    :@param side: side length
    :@return:perimeter of regular hexagon (units of side)
    >>> regular_hexagon_perimeter(6)
    36
    """
    return side*6


def regular_hexagon_area(side):
    """
    calculate the area of a regular hexagon from side length.
    :@param side: the side length
    :@return:the area (units length^2)
    >>>return regular_hexagon_area(6)
    93.53
    """
    return ((3*math.sqrt(3))/2)*side**2


# calculate the perimeter and the area of circle#
def circle_perimeter(radius):
    """
    calculate the perimeter of a circle from radius.
    :@param radius: radius length
    :@return:perimeter of circle (units of radius)
    >>> circle_perimeter(8)
    50.26
    """
    return 2*pi*radius


def circle_area(radius):
    """
    calculate the area of a circle from radius.
    :@param radius: the radius
    :@return:the area (units radius^2)
    >>>return circle_area(8)
    201.06
    """
    return pi*radius**2


def cone_area(radius, height):
    """
    calculate the area of cone from radius and height.
    :@param radius: the radius of base.
    :@param height: the height of cone.
    :@return:The total surface area of cone (units^2 from radius).
    >>>cone_area(8,3)
    415.79
    """
    return pi*radius*(radius+math.sqrt(radius**2 + height**2))


def cone_volume(radius, height):
    """
    calculate the volume of cone.
    :@param radius: the radius of base.
    :@param height: the height of cone.
    :@return: the volume of cone(units^3 from radius).
    >>>cone_volume(8,3)
    201.06
    """
    return (pi*radius**2*height)/3


#calculate the area and the volume of cube

def cube_area(edge):
    """
    calculate the area of cube.
    :@param edge: the edge of cube.
    :@return:the area of cube(units^2from edge).
    >>>cube_area(10)
    600
    """
    return 6*(edge**2)


def cube_volume(edge):
    """
    calculate the volume of cube
    :@param edge: the edge of cube
    :@return:the volume of cube(units**3from edge)
    >>>cube_volume(10)
    1000
    """
    return edge**3

print("cube_area =", cube_area(10), ";", "cube_volume =", cube_volume(10))


def cuboid_volume(length, width, height):
    #calculate the volume of cuboid
    """

    :@param length: the length of the cuboid
    :@param width: the width of the cuboid
    :@param height:the height of the cuboid
    :@return:the volume of cuboid(units**3 from length)
    >>> cuboid_volume(9,5,3)
    135
    """
    return length*width*height

print("cuboid_volume =", cuboid_volume(9, 5, 3))


#calculate the area of sphere
def sphere_area(radius):
    """

    :@param radius: the radius of sphere
    :@return:the area of sphere(units^2 from radius)
    >>>sphere_area(8)
    804,5
    """
    return 4*pi*radius**2


#calculate the volume of cylinder.
def cylinder_volume(radius, height):
    """
    calculate the volume of cylinder
    :@param radius: the radius of cylinder
    :@param height: the height of cylinder
    :@return:the volume of cylinder(units^3 from radius)
    >>>cylinder_volume(8,3)
    552.92
    """
    return 2*pi*radius*(radius+height)


if __name__ == "__main__":
    s_side = 4
    s_length = 9
    s_width = 8
    s_height = 3
    s_radius = 8
    s_edge = 10
    print("perimeter = ", s_side*4, " ;", "area = ", s_side*s_side)
    print("rectangle_perimeter = ", (s_length + s_width)*2, ";", "rectangle_area = ", s_length*s_width)
    print("triangle_perimeter = ", s_length+s_side+s_height, ";", "triangle_area = ", (s_side*s_height)/2)
    print("trapezium_perimeter = ", s_length+s_width+s_side+s_height, " ;", "trapezium_area = ",
          ((s_length+s_width)*s_height)/2)
    print("regular_hexagon_perimeter = ", s_side*6, ";", "regular_hexagon_area = ", ((3*math.sqrt(3))/2)*s_side**2)
    print("circle_perimeter = ", 2*pi*s_radius, ";", "circle_area = ", pi*s_radius**2)
    print("cone_area =", cone_area(s_radius, s_height), ";", "cone_volume =", cone_volume(s_radius, s_height))
    print("cylinder_volume =", cylinder_volume(8, 3))