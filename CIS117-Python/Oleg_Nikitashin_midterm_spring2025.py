# Midterm Spring 2025
# Instructions: Replace all ___?___ below to complete the code
#               ONLY replace the ___?___
# Name:Oleg Nikitashin


def longest_word(sentence):
    """Returns the longest word in the given sentence."""
    words = sentence.split()  
    max_length = 0
    longest = ""

    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word
    
    return longest

def most_frequent(lst):
    """Returns the most frequent element in the list."""
    freq_dict = {}  

    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    
    max_freq = 0
    most_common = None

    for key, value in freq_dict.items():
        if value > max_freq:
            max_freq = value
            most_common = key

    return most_common

def reverse_words(sentence):
    """Returns a sentence with each word reversed but in the same order."""
    words = sentence.split()  
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)  

    return " ".join(reversed_words)  

def count_unique_words(sentence):
    """Returns a dictionary with word counts from the given sentence."""
    words = sentence.lower().split()  # Convert sentence to lowercase and split into words
    word_counts = {}  # Dictionary to store word frequencies

    for word in words:
        if word in word_counts:
            word_counts[word] += 1  
        else:
            word_counts[word] = 1  
    
    return word_counts

def is_prime(n):
    """Returns True if n is a prime number, otherwise False.
       In case you forgot, prime numbers can only be divided by 1 and itself"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True


##### Test cases (do not modify) #####


test_sentences = [
    "Python programming is fun",
    "AI models struggle with incomplete logic",
    "Keep coding and learning"
]

for sentence in test_sentences:
    print(f"Longest word in '{sentence}': {longest_word(sentence)}")
print('--------------------------------------------------')

test_lists = [
    [1, 2, 3, 1, 2, 1, 4, 1],
    ["apple", "banana", "apple", "orange", "banana", "apple"],
    [True, False, True, True, False, False, False]
]

for lst in test_lists:
    print(f"Most frequent in {lst}: {most_frequent(lst)}")
print('--------------------------------------------------')

for sentence in test_sentences:
    print(f"Original: {sentence}")
    print(f"Reversed: {reverse_words(sentence)}")
    print()
print('--------------------------------------------------')

test_sentences = [
    "This is a test. This test is simple.",
    "Hello world! Hello again, world.",
    "Python is fun. Python is powerful. It is just great."
]

for sentence in test_sentences:
    print(f"Sentence: {sentence}")
    print(f"Word Counts: {count_unique_words(sentence)}")
    print()
print('--------------------------------------------------')

test_numbers = [2, 3, 10, 17, 20, 23, 31]
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")

