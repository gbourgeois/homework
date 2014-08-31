__author__ = 'bourgeois'
import math
from math import pi


print("I was taught Python3 course. Hello bourgeois")

#CIRCLE
#Perimeter of a Circle
def circle_perimeter(radius):
    '''
    Calculate perimeter of a circle from radius
    :param radius: the radius
    :return: the perimeter (same units as the radius)
    '''
    return 2*pi*radius

print("The perimeter of my circle is ", circle_perimeter(10))

#Area of a Circle
def circle_area(radius):
    return pi*radius*radius
    '''
    Calculate area of a circle from radius
    :param radius: the radius
    :return: the perimeter (units^2 from radius)
    '''

print("The area of my circle is ", circle_area(10))

#PARALLELOGRAM
#Perimeter of a parallelogram
def parallelogram_perimeter(side1,side2):
    return 2*(side1+side2)
print (parallelogram_perimeter(2,4))
#Area of Parallelogram
def parallelogram_area(base,height):
    return base*height
print (parallelogram_area(3,5))
