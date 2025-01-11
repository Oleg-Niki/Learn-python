file_obj = open('file1.txt', "r")

print("Is the file closed? ", file_obj.closed)

print("Name of the file: ", file_obj.name)

print("Mode of the file: ", file_obj.mode)

file_obj.close()

print("Is the file closed? ", file_obj.closed)

#with statement
with open('file1.txt', 'r') as file_obj:
    print("Is the file closed? ", file_obj.closed)

    print("Name of the file: ", file_obj.name)

    print("Mode of the file: ", file_obj.mode)
    
print("Is the file closed? ", file_obj.closed)

with open ('file1.txt', 'r') as file_obj2:
    content = file_obj2.read(4)
    print(content)
    
with open ('file1.txt', 'w') as file_obj3:
    file_obj3.write("This is a new line")
    
with open ('file1.txt', 'r') as file_obj4:
    content = file_obj4.read()
    print(content)