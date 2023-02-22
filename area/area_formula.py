# area of circle.
import math


def area_of_circle(radius):
    result = math.pi* radius * radius
    return result


def area_of_triangle(base, height):
    return base * height / 2

def area_of_square(side):
    return side*side

def area_of_trapezium(small_base,large_base,height):
    return (small_base+large_base)/2*height