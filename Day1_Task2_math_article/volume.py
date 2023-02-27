import math

def volume_of_sphere(radius):
    return 4*math.pi*math.pow(radius,3)/3

def volume_of_cylinder(radius,height):
    return math.pi*radius*radius*height

def volume_of_cone(radius,height):
    return math.pi*radius*radius*height/3

def volume_of_hemisphere(radius):
    return 2*math.pi*math.pow(radius,3)/3