# Filter in Python --> always work with function
# the filter() function is built-in function in python
# allows you to filter the element in list, tuple, set
# it only work with function which give True and False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# filter on the above --> get even number -->
# new-list_even = [2, 4, 6, 8, 10]


def is_even(num):
    return num % 2 == 0


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))


# we can apply a filter on each element of a list, id true then it will in new list if false then not in list


def is_greater_5(num):
    return num > 5


new_numbers_five = filter(is_greater_5, numbers)
print(list(new_numbers_five))
