#29. Sentence Reversal


s = input("Enter a sentence: ")

words = s.split()
words.reverse()

print("Reversed sentence:", " ".join(words))