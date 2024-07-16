# Develop a python script that calculate the square and cube of a given number
a = int(input("Enter a number:"))
b = a*a
c = a*a*a
print("square of a is:", b)
print("cube of a is:", c)
p = pow(a, 2)


def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

print("-----------------------------------Or-----------------------")
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate squares
squares = [num ** 2 for num in numbers]

# Calculate cubes
cubes = [num ** 3 for num in numbers]

# Print the lists
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)