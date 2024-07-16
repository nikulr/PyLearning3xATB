# Data Type - List
# List -- shopping list
# Add item
# Remove item
# Update item
# view item

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))
print(shopping_list[1])
print(shopping_list[-1])


shopping_list.append("Curd")  # append add item in the end
print(shopping_list)

shopping_list.insert(1, "Jam")  # add item in middle
print(shopping_list)

shopping_list.extend(["Chips", "Salt"])
print(shopping_list)

shopping_list.remove("bread")
print(shopping_list)
print(shopping_list.index("Jam"))

shopping_list.reverse()
print(shopping_list)

shopping_list.sort()
print(shopping_list)

shopping_list[0] = "Pramod"
print(shopping_list)

print("----------------------------------------------------------------------")

#  list with different data types:

my_list = [1, 2, 3, 4, True, 10.11, 12.45, "Pramod", 3.14]
print(my_list)
print(len(my_list))
print(my_list[2])
print(my_list[-1])
print(type(my_list))





