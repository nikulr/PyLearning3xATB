# 1. Explain the difference between the = operator and == operator in python
'''
Identity vs Equality operators:

= is used for assignation of value --> Identity operator (is)
== is used for comparison of two variable,list or string --> equality operator

The = is a simple assignment operator. It assigns values from right side operands to the left side operand.

While on the other hand == checks if the values of two operands are equal or not. If yes, the condition becomes true and it returns a non zero value.

For example,

a=10 #The value 10 will be stored in the integer variable a.

if(a==10): #This will check if the value stored in variable a is equal to 10. If yes it will return a non zero value.

https://byjus.com/gate/difference-between-equality-and-identity-operator-in-python/#:~:text=Difference%20between%20%3D%3D%20and%20is%20operators%20in%20Python,compare%20the%20two%20objects'%20values.

'''

a=10
b=10

# Case 1:
# Return True because both a and b have the same value
print(a==b)

# Case 2:
# Return True because both a and b is pointing to the same object
print(id(a))
print(id(b))

print(a is b)


# Case 3:
# Here variable a is assigned to new variable c,
# which holds same object and same memory location
c=a
id(c)
print(c)
print(c is a)

# 2. What does the ** operators do in python, and how is it used?
'''
** --> Exponentiation Operator

In Python, ** is the exponentiation operator. Furthermore, i to raise the first operand to power of second.
'''
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2



# 3. what does the ^ operators do in python, and in what context is it commonly used?
# ^ --> Bitwise operators are used to compare (binary) numbers:
# https://www.w3schools.com/python/python_operators.asp

print(10 ^ 3)

"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""