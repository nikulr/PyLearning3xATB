# Logical Operators
'''
and
or
not
'''

T = True
F = False
print("The Value of T and F is:", (T and F))
print("The Value of T or F is:", (T or F))
print("The Value of T not F is:", (not F))

print("-------------------other example-------------------")

a = 10
b = 45
x = 15
y = 67
result1 = (a > b)  # false
result2 = (x < y)  # true
result3 = result1 and result2  # false and True
print(result3)

result4 = result1 or result2  # false and True
print(result4)



