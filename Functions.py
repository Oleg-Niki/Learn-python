num1 = int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))

#Defining a function to add two numbers
def add_num(num1, num2):
    sum = num1+num2
    return sum

final_value = add_num(num1, num2)
print("The sum of the two numbers is: ", final_value)

x,y=10,20

value = add_num(x,y)
print("The sum of X and Y: ", value)

def quadratic_eqn(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x1, x2

print('Lets solve the quadratic equation: ax^2 + bx + c = 0')
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
result = quadratic_eqn(a,b,c)
print("The roots of the quadratic equation are: ", result)

def personal_info(name, age=35):
    print("Name: ", name)
    print("Age: ", age)
    
name = "Oleg"
age = 37

personal_info(name, age)

personal_info(name)

def personal_info(*args):
    for value in args:
        print(value)
        
personal_info('Oleg' , 'Nik', 'Male', '37')
