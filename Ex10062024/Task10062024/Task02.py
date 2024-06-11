# Develop a python script that calculate the square and cube of a given number
a = int(input("Enter a number:"))
b = a*a
c = a*a*a
print("square of a is:", b)
print("cube of a is:", c)
p = pow(a, 2)


# create a program that takes two numbers as input and prints wether the first number is greater than, less than, or equal to the second number

num1 = int(input("Enter first number:"))
num2 = int(input("Enter first number:"))

print(num1,"is greater") if (num1 > num2) else print(num2,"is greater")

# or

print("Both num1 and num2 are equal" if num1 == num2 else "num1 is greater  than num2" if num1 > num2 else "num2 is greater than num1")