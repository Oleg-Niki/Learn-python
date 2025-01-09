from filecmp import cmp


tuple_1 = ('a', 'b', 'c', 'd', 'e')
print(type(tuple_1))
print("Contents of tuple_1: ", tuple_1)

tuple_2 = ('Ram',)
print(type(tuple_2))
tuple_3 = ('Ram')
print(type(tuple_3))

# Accessing elements of a tuple
print("Contents of tuple_1: ", tuple_1)
print("Element at index 1: ", tuple_1[1])
print("Element at index 4: ", tuple_1[4])
print("Fourth letter", tuple_1[3])
print("Last letter", tuple_1[-1])

# Slicing a tuple
print("Elements from index 1 to 3: ", tuple_1[1:4])
print("Elements from index 2 to end: ", tuple_1[2:])
print("Elements from start to index 2: ", tuple_1[:3])
print("All elements: ", tuple_1[:])
print("Starting from the first to last with step 2: ", tuple_1[::2])

# Updating a tuple
tuple_4 = (100, 200, 300)
print("Elements inside tuple_1 are", tuple_1)
print("Elements inside tuple_4 are", tuple_4)
tuple_5 = tuple_1 + tuple_4
print("Elements inside tuple_5 are", tuple_5)
tuple_6 = tuple_4 * 3
print("Elements inside tuple_6 are", tuple_6)

# Deleting a tuple
del tuple_6
print("tuple_6 is deleted")