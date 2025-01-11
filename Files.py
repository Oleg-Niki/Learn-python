f = open("practice_file.txt", "w+")
f.write("Hello World \nThis is a practice file_FIRST LINE \nThis is the second line \nThis is the third line")
f = open("practice_file.txt", "r")
content = f.read()
print(content)

f = open("practice_file.txt", "a")
f.write("\nThis is the fourth line appended to the file")
f = open("practice_file.txt", "r")
lines = f.readlines()
lines_count = len(lines)
print("in this file at this moment we have" , lines_count, "lines")

print("Ask the word you want to search in the file:")
word = input()
f = open("practice_file.txt", "r")
word_count = 0
for line in f:
    words = line.split()
    for i in words:
        if i == word:
            word_count += 1
print("The word", word, "is found", word_count, "times in the file")

print("Ask the word you want to replace in the file:")
word_replace = input()
print("Ask the word you want to replace with:")
word_replace_with = input()
f = open("practice_file.txt", "r")
content_replace = f.read()
content_replace = content_replace.replace(word_replace, word_replace_with)
f = open("practice_file.txt", "w")
f.write(content_replace)
f = open("practice_file.txt", "r")
content = f.read()
print(content)

f.close()