# Fibonacci Series - # Program to display the Fibonacci sequence up to n-th term
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.
# Fibonacci series upto 10 terms is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13
# def fibonacci(n):
#     a, b = 0, 1
#     fibonacci_series = [a, b]
#     for _ in range(2, n):
#         a, b = b, a + b
#         fibonacci_series.append(b)
#     return fibonacci_series
#
# Fn = Fn-1 + Fn-2
# with seed values : F0 = 0 and F1 = 1.
#
# https://prepinsta.com/python-program/find-fibonacci-series-up-to-n/
# https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
#
#  Example

num = int(input("Enter a range for the fibonacci series: "))
sum = 0
fibonacci_series = []

for i in range(num):
    if sum == 0:
        sum = sum + i
        fibonacci_series.append(sum)
    else:
        fibonacci_series.append(sum)
        sum = sum + fibonacci_series[i - 1]

print(fibonacci_series)

print("====================== Another way ========================")

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print("----------------------------------------------------")

n = 10
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

