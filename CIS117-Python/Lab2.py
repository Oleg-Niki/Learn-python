# CIS-117 Lab2
# Description: This module contains functions that check for various alphabetical "antics":
#              Palindrome, Pangram, Tautogram, Isogram, Abecederian, and Dobloon.
# Group#: <your group number>
# Names: <Partner 1: Oleg Nikitashin, Partner 2: Hazel Juarez >

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

# FUNCTION is_palindrome(text):
#     1. Convert text to lowercase.
#     2. Remove all non-alphabetic characters (optional) or at least strip spaces.
#     3. Set reversed_text = reverse of the cleaned text.
#     4. IF cleaned text is EQUAL to reversed_text:
#         RETURN True
#        ELSE:
#         RETURN False


def is_palindrome(text):
    """
    Checks if the given text is a palindrome.
    Ignores case and optionally non-alphabetic characters.
    Returns True if palindrome, False otherwise.
    """
    
    # 1. Convert text to lowercase. (COULD BE WRONG!!!!!!!!!!!!! NEED TO DOUBLE CHECK)
    lowercase_text = text.lower()
    # 2. Remove all non-alphabetic characters (optional) or at least strip spaces.
    # Input string
    s1 = lowercase_text

    # Use list comprehension to keep only alphanumeric characters
    s2 = ''.join([char for char in s1 if char.isalnum()])

    # Print the cleaned string
    print(s2)
    
    # 3. Set reversed_text = reverse of the cleaned text.




# FUNCTION is_pangram(text):
#     1. Convert text to lowercase.
#     2. Initialize an empty set to track letters found, e.g. found_letters = {}.
#     3. FOR each character in text:
#         a. IF character is a letter (a–z):
#             - Add character to the found_letters set.
#     4. IF the size of found_letters is 26:
#         RETURN True
#        ELSE:
#         RETURN False
        

# FUNCTION is_tautogram(text):
#     1. Convert text to lowercase.
#     2. Split text into a list of words.
#     3. IF there are no words, return False (or handle as appropriate).
#     4. Get the first letter of the first word (call this initial_letter).
#     5. FOR each word in the list of words:
#         a. IF the first letter of the current word is NOT the same as initial_letter:
#             RETURN False
#     6. IF the loop completes with no mismatch:
#         RETURN True
        
        
# FUNCTION is_isogram(word):
#     1. Convert word to lowercase.
#     2. Remove all non-alphabetic characters if necessary.
#     3. Create an empty set called letters_seen.
#     4. FOR each character in word:
#         a. IF character is in letters_seen:
#             RETURN False
#         b. ELSE:
#             Add character to letters_seen
#     5. IF the loop finishes with no repeats found:
#         RETURN True

# FUNCTION is_abecederian(word):
#     1. Convert word to lowercase.
#     2. Remove all non-alphabetic characters if necessary.
#     3. Create a sorted version of the letters, call it sorted_word.
#     4. IF sorted_word is EQUAL to the original word (after cleaning):
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