#28. Word Frequency Dictionary

s = input("Enter a paragraph: ")

words = s.split()

for word in set(words):
    print(word, ":", words.count(word))