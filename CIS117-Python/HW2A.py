#1
# Homework 2A
# Author: Oleg Nikitashin   
# Date: 1/22/2025

#2
# Print a hello message on the screen introducing yourself
print("Hello, my name is Oleg")

#3 
# Assign your student id number to a variable named my_id (ignore leading zeros) 
my_id = 1336725

#4
# Print the value in my_id:
# - as integer padded with zeros if less than 8 digits (for example, 12345 should be printed as 00012345)
print(f"{my_id:08}")
# - with two decimals (12345 should be printed as 12345.00)
print(f"{my_id:.2f}")
# - as a binary number (12345 should be printed as 11000000111001)
print(f"{my_id:b}")
# - as a hexadecimal number (12345 should be printed as 0x3039)
print(f"{my_id:#x}")

#5
# Use the // operator to extract the first digit of your student id number and assign the value to a variable named first.
print(my_id // 1000000)
first = my_id // 1000000

#6
# Use the % operator to extract the last digit of your student id number and assign the value to a variable named last.
print(my_id % 10)
last = my_id % 10

#7
# Print the result of adding first + last on the screen.
print(first + last)


