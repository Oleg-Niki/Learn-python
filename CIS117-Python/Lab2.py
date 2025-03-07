# CIS-117 Lab2
# Description: This module contains functions that check for various alphabetical "antics":
#              Palindrome, Pangram, Tautogram, Isogram, Abecederian, and Dobloon.
# Group#: 15
# Names: Partner 1: Oleg Nikitashin (last 3 functions), Partner 2: Hazel Juarez (first 3 functions)

"""
Module: Antics

This module defines six functions:
1. is_palindrome(text)
2. is_pangram(text)
3. is_tautogram(text)
4. is_isogram(word)
5. is_abecederian(word)
6. is_dobloon(word)
"""

# 1. FUNCTION is_palindrome(text):
#     1.1. Convert text to lowercase.
#     1.2. Remove all non-alphabetic characters (optional) or at least strip spaces.
#     1.3. Set reversed_text = reverse of the cleaned text.
#     1.4. IF cleaned text is EQUAL to reversed_text:
#         RETURN True
#        ELSE:
#         RETURN False

def palindrome(text):
    """
    Checks if the given text is a palindrome.
    Ignores case and non-alphabetic characters.
    Returns True if palindrome, False otherwise.
    """
    name = text.lower()
    clean_name = ''.join(char for char in name if char.isalnum()) #string free of spaces, punctuation, and special characters
    word = ''
    for i in clean_name:
        if 'a' <= i <= 'z':
            word += i
            print("Your enter is: ",word)
        
    return word == word[::-1]

# 2 . FUNCTION is_pangram(text):
#     2.1. Convert text to lowercase.
#     2.2.1 OPTION 1: Initialize an empty set to track letters found, e.g. found_letters = {}.
#     2.2.2. FOR each character in text:
#         a. IF character is a letter (a–z):
#             - Add character to the found_letters set.
#     2.2.3. IF the size of found_letters is 26:
#         RETURN True
#        ELSE:
#         RETURN False
#     2.3.1 OPTION 2: make a string alphabet and loop it thru that range

def pangram(text):
    """
    Checks if sentence containing all 26 letters of the alphabet
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for letter in alphabet:
        if letter not in text:
            return False
    return True
        

# 3. FUNCTION is_tautogram(text):
#     1. Convert text to lowercase.
#     2. Split text into a list of words.
#     3. optional: IF there are no words, return False (or handle as appropriate).
#     4. Get the first letter of the first word (call this initial_letter).
#     5. FOR each word in the list of words:
#         a. IF the first letter of the current word is NOT the same as initial_letter:
#             RETURN False
#     6. IF the loop completes with no mismatch:
#         RETURN True
def tautogram(text):
    """
    Checks if all words start with the same letter
    """
    sentence = text.lower().split()

    first_letter = sentence[0][0]

    for word in sentence:
        if word[0] != first_letter:
            return False
    return True
        
        
# 4. FUNCTION is_isogram(word):
#     4.1. Convert word to lowercase.
#     4.2. Remove all non-alphabetic characters if necessary.
#     4.3. Create an empty set called letters_seen.
#     4.4. FOR each character in word:
#         a. IF character is in letters_seen:
#             RETURN False
#         b. ELSE:
#             Add character to letters_seen
#     4.5. IF the loop finishes with no repeats found:
#         RETURN True

def isogram(text):
    """
    Check if a word is an isogram (no repeating letters).
    """
    text = text.lower()
    clean_text = ''.join(char for char in text if char.isalnum()) #string free of spaces, punctuation, and special characters
    letters_seen = set()
    for char in clean_text:
        if char in letters_seen:
            return False
        letters_seen.add(char)
        
    return True
            
# 5. FUNCTION is_abecederian(word):
#     5.1. Convert word to lowercase.
#     5.2. Remove all non-alphabetic characters if necessary.
#     5.3. Create a sorted version of the letters, call it sorted_word.
#     5.4. IF sorted_word is EQUAL to the original word (after cleaning):
#         RETURN True
#        ELSE:
#         RETURN False
        

# FUNCTION is_dobloon(word):
#     1. Convert word to lowercase.
#     2. Remove all non-alphabetic characters if necessary.
#     3. Create a dictionary (or a Counter) to count occurrences of each letter.
#     4. FOR each letter in the word:
#         - Increase the count of that letter in the dictionary.
#     5. FOR each letter in the dictionary:
#         a. IF the count of that letter is not exactly 2:
#             RETURN False
#     6. IF all letters have count = 2:
#         RETURN True

if __name__ == "__main__":
    while True:
        print("hello user! choose your function:")
        print("1. Palindrome")
        print("2. Pangram")
        print("3. Tautogram")
        print("4. Isogram")
        print("To be continued...")
        user_input = input("Enter your choise (or 'q' to quit) : ")
        
        if user_input == "1":
            user_word = input("Enter your word: ")
            result = palindrome(user_word)
            print("Is Palindrome? the result is: ", result)
        elif user_input == '2':
            user_word = input("Enter your word: ")
            result = pangram(user_word)
            print("Is Pangram? the result is: ", result)
        elif user_input == '3':
            user_word = input("Enter your text: ")
            result = tautogram(user_word)
            print("Is Tautogram? the result is: ", result)
        elif user_input == '4':
            user_word = input("Enter your text: ")
            result = isogram(user_word)
            print("Is Isogram? the result is: ", result)
            
        elif user_input.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Invalid choice, please read the instructions above")