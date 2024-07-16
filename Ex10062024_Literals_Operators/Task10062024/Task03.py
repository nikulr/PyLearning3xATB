# create a program that takes two numbers as input and prints wether the first number is greater than, less than, or equal to the second number

num1 = int(input("Enter first number:"))
num2 = int(input("Enter first number:"))

print(num1,"is greater") if (num1 > num2) else print(num2,"is greater")

# or

print("Both num1 and num2 are equal" if num1 == num2 else "num1 is greater  than num2" if num1 > num2 else "num2 is greater than num1")