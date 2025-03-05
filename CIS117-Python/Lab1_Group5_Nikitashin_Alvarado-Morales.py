"""
Lab 1
Group #5
Authors: 
    - Partner1: <Oleg Nikitashin> (Guessing Game)
    - Partner2: <Jeyden Alvarado-Morales> (Rock-Paper-Scissors)
Date: <03/04/2025>

Description:
    This program is two simple games:
    1) Guessing Game
    2) Rock-Paper-Scissors

    The user can choose which game to play. Each game is implemented in
    its own function. The main program (entry-point) asks for the user’s
    choice and then calls the corresponding function. There is a loop
    so the user can play multiple rounds.
"""

import random

def guessing_game():
    """
    Author: Oleg
    --------------------------------------------------
    Guessing Game:
    1) Generates a random number (1–10) 
    2) The user has 5 attempts
    3) Lets user know it 'Too low' or 'Too high'
    4) Lets the user decide to play again
    --------------------------------------------------
    """
    while True:
        #generate a random number
        secret_number = random.randint(1, 10)
        #set the number of current attempts and max
        attempts = 0
        max_attempts = 5
        print("I'm thinking of a number between 1 and 10, guess what number........")

        while attempts < max_attempts:
            print("You current attempt: ", attempts + 1, "of", max_attempts)
            user_enter = input("Please enter your guess: ") #we may need verification of an integer but let's continue as is for now
            user_guess = int(user_enter)
            print("You entered: ", user_guess)
                    
            if user_guess == secret_number:
                print("You win")
                break
                                
            elif user_guess > secret_number:
                print("Too hing")
                            
            else:
                print("Too low")
                
            attempts +=1
                
        if attempts == max_attempts:
            print("You run out of attempts")
        
        print("The number I was thinking of is:", secret_number)
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again != 'y':
            print("...To main menu...")
            break
    
    
def play_rps():
    """
    Author: Jeyden
    --------------------------------------------------
    Rock-Paper-Scissors game:
    1) The user is prompted to pick 1 (paper), 2 (scissors), or 3 (rock).
    2) A random choice for the computer is generated.
    3) The result is determined (win, lose, tie).
    4) Lets the user decide to play again
    --------------------------------------------------
    """
    while True:
        print("\nWelcome to Rock-Paper-Scissors!")
        print("1 -> Paper")
        print("2 -> Scissors")
        print("3 -> Rock")

        user_input = input("Enter your choice (1, 2, or 3): ")
        
        # Validate that the user_input is a digit and in the correct range
        if not user_input.isdigit():
            print("Invalid choice. Please enter a number (1, 2, or 3).")
            continue

        user_choice = int(user_input)
        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        # Map numbers to strings
        choices = {1: "paper", 2: "scissors", 3: "rock"}
        computer_choice = random.randint(1, 3)

        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        # Determine the result
        if user_choice == computer_choice:
            print("It is a tie!")
        elif (
            (user_choice == 1 and computer_choice == 3) or
            (user_choice == 2 and computer_choice == 1) or
            (user_choice == 3 and computer_choice == 2)
        ):
            print("You win!")
        else:
            print("You lose!")

        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Returning to main menu...\n")
            break

if __name__ == "__main__":
    while True:
        print("Which game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-paper-scissors")
        user_input = input("Enter your choice (or 'q' to quit): ")
    
        if user_input == '1':
            guessing_game()
        elif user_input == '2':
            play_rps()
        elif user_input.lower() == 'q':
            print("Thanks for playing! See you again")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 'q' to quit.")
    
    