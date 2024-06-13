# Task 3
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

# Using for
num = int(input("Enter the number: "))
factorial_val = 1
for i in range(num, 0, -1):
    factorial_val *= i
print('The factorial value of ',str(num), ' is ', str(factorial_val))

# Using for loop
Num2 = int(input("Enter number: "))
Fact1 = 1
for i in range(1, Num2 + 1):
    Fact1 = Fact1 * i
    print(i, end=' ')
    if i < Num2:
        print("*", end=' ')
print("\nFactorial: ", Fact1)

# Using while loop
Num = int(input("Enter number: "))
Fact = 1
while Num > 0:
    Fact = Fact * Num
    Num = Num - 1

print(Fact)