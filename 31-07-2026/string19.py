#a.	Count how many times a specific word appears in a sentence. 

str = input("Enter a sentence: ")

word = input("Enter a word to calculate frequency: ")

count = 0

for i in str.split():
    if i == word:
        count = count + 1

print("The word", word, "is repeated", count, "times")