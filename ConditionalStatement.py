number = int(input("Enter a number: "))

if (number >0): 
    print ("Entered inside the parent if block")
    if (number>10):
        print("Entered inside nested if block")
        
    print("Exited from nested if block")

print("Control flows out of the parent if block")

print("positive") if number > 0 else print("negative")
