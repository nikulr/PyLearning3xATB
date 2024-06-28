# MAP vs Filters  --> Very Important

# MAP
# it pick 1 item and apply the function
# give the same number of elements


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_me(num):
    return num * 2


new_list_double = map(double_me, numbers)
print(list(new_list_double))


# using Lambda

# double_me_lambda = lambda n:n * 2
#
# new_list_double = map(double_me_lambda, numbers)
# print(list(new_list_double))


print("-----------------------------------------------------------")

# Filters  -->
# it pick 1 item --> if true then keep it, if false, remove it
# give the less numbers of items as compared to actual

def is_even(num):
    return num % 2 == 0


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))