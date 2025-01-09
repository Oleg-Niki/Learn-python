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