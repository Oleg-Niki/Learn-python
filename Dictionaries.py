dict_1 = {'key1': 'value1', 'key2': 'value2', 'key3' : 'value3'}
print(dict_1)
print(dict_1['key1'])
dict_2 = {'Fruits': ['Apple', 'Banana', 'Orange'], 'Vegetables': ['Carrot', 'Potato', 'Onion'], 1:['One', 'Two', 'Three']}
print(dict_2['Fruits'])

dictionary = dict({1:'Virat', 2:'Rohit', 3:'Dhoni'})
print("the dictionary is: ", dictionary)
dictionary_2 = dict([(1,'Sky'), (2,'Earth'), (3,'Ocean')])
print("the dictionary 2 is: ", dictionary_2)

# Accessing elements from a dictionary
print("Value of Key2 in dict1: ", dict_1['key2'])
for i in dict_1:
    if i == 'key3':
        print("The value of key3 is: ", dict_1[i])
        
# Updating elements in a dictionary
dict_2['Fruits'] = ['Cocaine', 'Heroin']
print("Updated Fruits in dict2: ", dict_2['Fruits'])
dict_2['Vegetables'] = ['Cannabis', 'Meth']
print("Updated Vegetables in dict2: ", dict_2['Vegetables'])

# Adding elements to a dictionary
dict_2['Cigs'] = 'Marlboro' , 'Camel'
print("Updated dict2 with Cigs: ", dict_2)

# Deleting elements from a dictionary
del dict_2['Cigs']
print("Deleted Cigs from dict2: ", dict_2)
removed_item = dict_2.pop('Fruits')
print("Removed Fruits from dict2: ", removed_item)
print("Updated dict2 after removing Fruits: ", dict_2)
popped_item = dict_2.popitem()
print("Popped item from dict2: ", popped_item)
dict_2.clear()
print("Cleared dict2: ", dict_2)