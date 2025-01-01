Problem: Number Guessing Game
Write a Python program that lets a user play a number guessing game. The program should:

Randomly choose a number between 1 and 100 (inclusive).
Allow the user up to 10 attempts to guess the number.
Provide feedback after each guess:
"Too high!" if the guess is greater than the number.
"Too low!" if the guess is less than the number.
"Correct!" if the guess matches the number.
End the game if:
The user guesses the number correctly, or
The user runs out of attempts.
At the end of the game, display:
The correct number if the user didn't guess it.
The number of attempts used if they guessed correctly.
Example
Input/Output Example 1
yaml
Copy code
I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.
Enter your guess: 50
Too high!
Attempts remaining: 9
Enter your guess: 25
Too low!
Attempts remaining: 8
Enter your guess: 37
Correct! You guessed it in 3 attempts.
Input/Output Example 2
yaml
Copy code
I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.
Enter your guess: 80
Too low!
Attempts remaining: 9
Enter your guess: 90
Too low!
Attempts remaining: 8
Enter your guess: 99
Too high!
Attempts remaining: 7
Enter your guess: 95
Correct! You guessed it in 4 attempts.
Input/Output Example 3 (User runs out of attempts)
vbnet
Copy code
I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.
Enter your guess: 50
Too high!
Attempts remaining: 9
Enter your guess: 25
Too low!
Attempts remaining: 8
... (after more guesses)
Sorry, you're out of attempts. The number was 42.
Hints for Solving
Use the random.randint(1, 100) function to generate a random number.
Use a while loop to allow repeated guesses.
Use a break statement to exit the loop when the user guesses correctly.
Keep track of the number of attempts with a counter variable.