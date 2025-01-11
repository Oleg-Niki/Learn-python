file_name = "practice_file.txt"

# Write initial content
with open(file_name, "w") as f:
    f.write("Hello World \nThis is a practice file_FIRST LINE \nThis is the second line \nThis is the third line")

# Read and display content
with open(file_name, "r") as f:
    content = f.read()
print(content)

# Append content
with open(file_name, "a") as f:
    f.write("\nThis is the fourth line appended to the file")

# Count lines
with open(file_name, "r") as f:
    lines = f.readlines()
print(f"In this file at this moment, we have {len(lines)} lines")

# Search for a word
word = input("Enter the word you want to search in the file: ")
with open(file_name, "r") as f:
    word_count = sum(line.lower().count(word.lower()) for line in f)
print(f"The word '{word}' is found {word_count} times in the file.")

# Replace a word
word_replace = input("Enter the word you want to replace: ")
word_replace_with = input("Enter the word you want to replace it with: ")
with open(file_name, "r") as f:
    content = f.read()
content = content.replace(word_replace, word_replace_with)
with open(file_name, "w") as f:
    f.write(content)

# Display updated content
with open(file_name, "r") as f:
    updated_content = f.read()
print(updated_content)
