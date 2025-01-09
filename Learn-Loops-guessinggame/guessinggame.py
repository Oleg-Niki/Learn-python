import random
count_atmpts = 3
random_number = random.randint(1, 10)
print("Hello to my guessing game. Guess the number between 1 and 10, you have", count_atmpts, "attempts.")

while count_atmpts > 0:
    user_guess = int(input("Enter the number you guess: "))
    print("You entered: ", user_guess)

    if user_guess == random_number:
        print("WOW! Congrats! You guessed the correct number")1
        break
    elif user_guess < random_number:
        print("Your guess is lower than the correct number")
    else:
        print("Your guess is higher than the correct number")
    
    count_atmpts -= 1
    print("You have", count_atmpts, "chances left")

if count_atmpts == 0:
    print("Sorry, you've run out of attempts. The correct number was", random_number)
    
