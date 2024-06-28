# Recursion --> most Important and not easy to understand --> need to watch video multiple time and practice more

# Recursion is programming technique where function call itself in order to solve a problem

# two key concept need to undersatnd
# 1. Base case
# 2. Recursive case

# Factorial


def factorial(n):
    #base case:
    if n == 0 or n ==1:
        return 1

    # recursive case
    else:
        return n * factorial(n -1)


print(factorial(5))