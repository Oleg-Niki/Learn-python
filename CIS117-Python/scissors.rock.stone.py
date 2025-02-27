# Import the random module to let the computer choose a random option
import random

# Define a list of valid choices
CHOICES = ["scissors", "rock", "stone"]

def get_user_choice():
    """
    Prompt the user to enter their choice.
    Continue asking until a valid choice is given.
    """
    while True:
        print("Choose one: scissors, rock, or stone")
        user_input = input("> ").lower().strip()
        if user_input in CHOICES:
            return user_input
        else:
            print("Invalid input. Please choose 'scissors', 'rock', or 'stone'.")

def get_computer_choice():
    """
    Randomly select and return one of the valid choices for the computer.
    """
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the rules:
      - Rock crushes Scissors
      - Scissors cut Stone
      - Stone breaks Rock
    Returns "user", "computer", or "tie".
    """
    if user_choice == computer_choice:
        return "tie"
    
    # Check winning conditions for the user
    if ((user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "stone") or
        (user_choice == "stone" and computer_choice == "rock")):
        return "user"
    else:
        return "computer"

def play_game():
    """
    Main game loop:
      - Get choices from user and computer
      - Determine and display the result
      - Ask if the user wants to play again
    """
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
        else:
            print("Computer wins!")
        
        # Ask if the user wants to play again
        print("Do you want to play again? (yes/no)")
        play_again = input("> ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game if this file is executed directly
if __name__ == "__main__":
    play_game()
# This is a simple rock-paper-scissors game where the user plays against the computer.
# The game continues until the user decides to stop playing.
# The game is interactive and prompts the user for input.
# The computer's choice is random, and the winner is determined based on the rules of the game.