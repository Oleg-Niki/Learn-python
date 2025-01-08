#negative index in Python
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(list_1[-1])
print(list_1[-2])
print(list_1[-3])
print(list_1[-5])

#slicing in Python
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(list_1[1:5])
print(list_1[1:6])
print(list_1[4:])
print(list_1[1:])
print(list_1[:5])
print(list_1[:])
print(list_1[::2])

#updating the list
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list_1[3] = 'Z'
print(list_1)
list_1[1:3] = ['X', 'Y']
print(list_1)
list_1[1:5] = ['X', 'Y', 'Z', '1', '2', '3']
print(list_1)

#deleting elements from the list
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list_1.pop(1)
print(list_1)
list_1.remove('G')
print(list_1)

#list operations
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list_2 = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
print(list_1 + list_2)
print(list_1 * 2)
print('A' in list_1)
print('A' not in list_1)
print(len(list_1))
print(max(list_1))
print(min(list_1))
print(list(list_1))


#list methods
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list_1.append('K')
print(list_1)
list_1.extend(['L', 'M', 'N'])
print(list_1)
list_1.insert(1, 'Z')
print(list_1)
print(list_1.index('Z'))
list_1.reverse()
print(list_1)
list_1.remove('Z')
print(list_1)

#using the del keyword
list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
del list_1[1]
print(list_1)