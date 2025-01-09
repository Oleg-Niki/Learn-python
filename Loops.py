counter = 1
while (counter <= 5): print(2*counter) ; counter = counter+1 ; print("Value of the counter:" , counter)

#for loop
string_1 = "Hello World"

for iter_var in string_1:
    print("The character reached during traversal is:", iter_var)
    
#nested loops
list_1 = [1,2,3,4,5]
list_2 = ['Apple', 'Banana', 'Cherry', 'Dates', 'Elderberry']
for iter_var1 in list_1:
    print("The value of iter_var1 is:", iter_var1)
    for iter_var2 in list_2:
        print(iter_var2)
            
#break statement
list_1 = ['Apple', 'Banana', 'Cherry', 'Dates', 'Elderberry']
for iter_var1 in list_1:
    if iter_var1 == 'Cherry':
        break
    else:
        print("The value of iter_var1 is:", iter_var1)
        
#continue statement
list_1 = ['Apple', 'Banana', 'Cherry', 'Dates', 'Elderberry']
for iter_var1 in list_1:
    if iter_var1 == 'Cherry':
        print("This line is executed")
        continue
        print("This statement will not be printed")
    else:
        print("The value of iter_var1 is:", iter_var1)
        
#pass statement
list_1 = ['Apple', 'Banana', 'Cherry', 'Dates', 'Elderberry']
for iter_var1 in list_1:
    if iter_var1 == 'Cherry':
        print("This line is executed")
        pass
        print("This statement will be printed") 
    else:
        print("The value of iter_var1 is:", iter_var1)