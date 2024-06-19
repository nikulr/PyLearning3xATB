# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Equilateral Triangle: A triangle is said to be equilateral triangle if all the sides are equal. If X, Y, Z are three sides of the triangle. Then, the triangle is equilateral only if X = Y = Z.
#
# Isosceles Triangle: A triangle is said to be an isosceles triangle if any of its two sides are equal. If X, Y, Z are three sides of the triangle.Then, the triangle is isosceles if either X = Y or X = Z or Y = Z.
#
# Scalene Triangle: A triangle is said Scalene Triangle if none of its sides is equal.

Len_Side1 = float(input("Enter the length of 1st side: "))
Len_Side2 = float(input("Enter the length of 2nd side: "))
Len_Side3 = float(input("Enter the length of 3rd side: "))

if Len_Side1 == Len_Side2 == Len_Side3:
    print("Triangle is equilateral triangle ")
elif Len_Side1 == Len_Side2 or Len_Side2 == Len_Side3 or Len_Side1 == Len_Side3:
    print("Triangle is isosceles triangle")
else:
    print("Triangle is scalene triangle")
    
# triangle_type = classify_triangle(side1, side2, side3)
# print(f"The triangle is: {triangle_type}")