import random
print("Hello to my guessing game /n Guess the number between 1 and 10 /n Enter the number you guess:")
user_guess = int(input())
print("You entered: ", user_guess)

random_number = random.randint(1, 10)
if user_guess == random_number:
    print("You guessed the correct number")
elif user_guess != random_number:
    print("You guessed the wrong number")
    count = 3
    count -= 1
    print("You have", count, "chances left")
    print("The correct number is: ", random_number)
    
