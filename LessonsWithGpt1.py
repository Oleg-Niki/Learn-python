#Here’s a Python problem that tests a mix of programming concepts: logic, string manipulation, and basic data structures. Once you solve it, I can better understand your current level.

# Problem: Word Frequency Counter
# Write a Python program that takes a multiline string as input and performs the following tasks:

# Counts the frequency of each unique word in the string, ignoring case.
# Sorts the words alphabetically.
# Displays the top N most frequent words along with their counts, where N is provided by the user.
# Input
# A multiline string provided by the user.
# An integer N provided by the user.
# Output
# A list of the top N most frequent words and their counts, sorted alphabetically if they have the same frequency.

# Notes:
# Punctuation should not be counted as part of the word.
# Words are case-insensitive (e.g., "Test" and "test" are the same word).
# If two words have the same frequency, they should appear in alphabetical order.
# When you've solved it, share your code or let me know if you have any questions!
import re
from collections import Counter

user_input = input("Enter text to count words frequency here: ")
print("you entered: ", user_input)
user_input = user_input.lower() # convert to lowercase
user_input = re.sub(r'[^\w\s]', '', user_input) # remove punctuation

# split the string into words
words = user_input.split()
# count the frequency of each word
word_count = Counter(words)
# sort the words alphabetically
sorted_words = sorted(word_count.items(), key=lambda x: x[0])
# sort the words by frequency and then alphabetically
sorted_words = sorted(sorted_words, key=lambda x: x[1], reverse=True)
print("sorted_words: ", sorted_words)
print("word_count: ", word_count)

