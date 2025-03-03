"""
Lab 1
Group #X
Authors: 
    - Partner1: <Name> (Guessing Game)
    - Partner2: <Name> (Rock-Paper-Scissors)
Date: <Date>

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
    #generate a random number
    secret_number = random.randint(1, 10)
    #set the number of attempts
    attempts = 5
    #prompt the user to guess the number
    print("I'm thinking of a number between 1 and 10, guess what number........")
    user_enter = input("Enter number: ") #we may need verification of an integer but let's continue as is for now
    user_guess = int(user_enter)
    print("You entered: ", user_guess)
    
    # do while attempts == 5
    
    if user_guess == secret_number:
        print("Congrats! You win! Play again (Y or N)?")
        
        elif int(user_guess) < secret_number:
            print("Too low! Try again.")
            attempts += 1
        else:
            print("Too high! Try again.")
            attempts += 1
    
    print("The number I was thinking of is: ", secret_number)
    
    pass


    """
    Author: Partner1
    --------------------------------------------------
    This function implements the Guessing Game.
    1) Generate a random number within a specified range (e.g., 1–100).
    2) Ask the user to guess the number within a limited number of tries.
    3) Provide feedback: "Too high" or "Too low" after each guess.
    4) If the user guesses the number within the allowed tries, announce they won.
    5) Otherwise, reveal the correct number after all tries are used.
    6) Ask if the user wants to play again.

    Example flow:
        I'm thinking of a number between 1 and 100.
        Guess what it is. You have 5 tries: 50
        Nope! Too low. Try again (4 tries left): ...

    Returns:
        None
    --------------------------------------------------
    """
    # TODO: Implement the guessing game logic here.
    # Example steps/pseudocode:
    #
    # while True:
    #     secret_number = random.randint(1, 100)
    #     attempts = 5
    #     # loop for guesses
    #         # prompt user
    #         # compare guess to secret_number
    #         # provide feedback
    #         # decrement attempts
    #         # break if guessed correctly
    #     # after attempts, announce result
    #     # ask user if they want to play again; break if "N"/"n"
    #
    # pass
    pass


def rock_paper_scissors():
    """
    Author: Partner2
    --------------------------------------------------
    This function implements the Rock-Paper-Scissors game.
    1) Generate a random move (1, 2, or 3), mapping each number to
       either Rock, Paper, or Scissors.
    2) Prompt the user to choose (1, 2, or 3).
    3) Compare user choice and random choice:
       - Decide if the user won, the computer won, or if it's a tie.
    4) Ask if the user wants to play again.

    Mapping Example:
        1 -> Paper
        2 -> Scissors
        3 -> Rock

    Example flow:
        Do you want to play? yes
        Enter your choice: 1. paper, 2. scissors, 3. rock: 2
        It is a tie!

    Returns:
        None
    --------------------------------------------------
    """
    # TODO: Implement the rock-paper-scissors logic here.
    # Example steps/pseudocode:
    #
    # while True:
    #     computer_choice = random.randint(1, 3)
    #     user_choice = int(input("Enter your choice..."))
    #     # compare computer_choice vs user_choice
    #     # determine winner or tie
    #     # print result
    #     # ask user if they want to play again; break if "N"/"n"
    #
    # pass
    pass


if __name__ == "__main__":
    """
    Main section of the script. This is the program entry point.
    It will:
      1) Ask the user which game they want to play.
      2) Call the corresponding function.
      3) Provide a loop to allow the user to play multiple rounds
         (either by re-choosing the same game or switching games).
    """

    # TODO: Implement the main program logic here.
    # Example steps/pseudocode:
    #
    while True:
        print("Which game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-paper-scissors")
        user_input = input("Enter your choice (or 'q' to quit): ")
    
        if user_input == '1':
            guessing_game()
        elif user_input == '2':
            rock_paper_scissors()
        elif user_input.lower() == 'q':
            print("Thanks for playing! See you again")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 'q' to quit.")
    
    
    # Note: The above code is a template and needs to be filled in with
    # actual game logic and user interaction.
    # The TODO comments indicate where to implement the game logic.
    # Make sure to test each game thoroughly.
    # Ensure to follow the instructions and guidelines provided in the lab.
    # Remember to replace the placeholders with actual names and dates.