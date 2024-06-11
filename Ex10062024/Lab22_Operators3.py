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


# Ternary Operators

pramod_marks = 90
amit_marks = 97
# X > Y -> to do something - print("Promod")
# Y > X --> to do ssomething else - print("Amit")

print("Pramod" if pramod_marks > amit_marks else "Amit")

# if-else
if pramod_marks > amit_marks:
    print("Pramod is winner")
else:
    print("Amit is winner")