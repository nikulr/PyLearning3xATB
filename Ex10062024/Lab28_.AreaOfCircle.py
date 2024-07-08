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

radius = float(input("Enter the radius of the circle:"))
area = 3.14159 * radius **2

print(f"The are of the circle is: {area}")

print("-----------------------------------------------------")


import math
print(math.pi*(float(input("Enter the radius\n"))**2))


print("-----------------------------------------------------")

import math

def area(r):
    area = math.pi * pow(r,2)
    return print("Area of circle is:", area)

area(4)




