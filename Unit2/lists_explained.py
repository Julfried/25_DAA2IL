#List
numbers = [1,2,3,4]
print("A list of numbers: ", numbers)

# Slicing a list
first_number = numbers[0]
print("First number:", first_number)

# List can also contain mixed datatypes
# Mixed list
mixed_list = [1, "two", 3.0, [4,5]]
print("Mixed list:", mixed_list)
list_in_list = mixed_list[3]
print("List in mixed list:", list_in_list)
print("Length of mixed list:", len(mixed_list))

# Lists are mutable, which means we can change their contents after they have been created.
mixed_list[1] = 2
# Be careful when modifying lists, assigning new value will overwrite the old value.
mixed_list[1] = "fail" 
print("Modified mixed list:", mixed_list)

# Appending to a list
print(f"There are {len(numbers)} numbers in the list.")
numbers.append(5)
print(f"There are {len(numbers)} numbers in the list.")
print("Modified numbers list:", numbers)

# Creating a list using a loop
squares = []
for x in range(10):
    squares.append(x * x)
print("Squares:", squares)

# List comprehension is a more concise way to create lists.
squares = [x * x for x in range(10)]  # List comprehension to create a list of squares
print("Squares:", squares)