import math
from area import area_formula
from math_article import volume
# radius=1
# area=22*radius*radius/7
# print(area)

area_circle = area_formula.area_of_circle(1)
print(area_circle)

area_triangle = area_formula.area_of_triangle(2, 4)
print(int(area_triangle))

area_square = area_formula.area_of_square(4)
print(area_square)

area_trapezium = area_formula.area_of_trapezium(2, 2, 2)
print(area_trapezium)



print(math.pi)
print(math.sqrt(4))
print(volume.volume_of_sphere(1))

print("Exercise for Feb-17-2023")

print(volume.volume_of_sphere(1))
print(volume.volume_of_cone(1,1))
print(volume.volume_of_cylinder(1,1))
print(volume.volume_of_hemisphere(1))

