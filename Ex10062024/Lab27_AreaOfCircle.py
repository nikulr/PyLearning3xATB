# program - calculate area of circle
# input -> radius
# output -> area
import math

# data types
# input --> float
# output --> float

# core logic --> pi*r*r  , pi =3-14
# math.pi

radius = float(input("Enter the radius:"))
print(math.pi)
area = math.pi * (radius ** 2)
area2 = math.pi * (math.pow(radius, 2))
print(area)
print(area2)

print("-----------------OR-----------------")


def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area


print("----------------------OR---------------------")
