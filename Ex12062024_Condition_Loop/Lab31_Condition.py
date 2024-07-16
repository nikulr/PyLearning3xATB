# If-Else
# create a program that takes two numbers as input and prints wether the first number is greater than, less than, or equal to the second number

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > num2:
    print(num1, "is greater")
else:
    print(num2, " is greater")

print("-------------------------------------------------------------")

# problem to find max between two number

a = int(input("Enter first number:"))
b = int(input("Enter first number:"))

result = max(a,b)
print("Max number is:", result)
