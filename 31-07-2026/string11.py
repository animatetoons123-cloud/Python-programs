# Longest Word 
# Find the longest word in a given sentence. 

str=input("Enter a string :")
word=" "
longest=" "
for i in str:
    if i != " ":
        word = word + i
    else:
        if len(word) > len(longest):
            longest = word
        word = ""


if len(word) > len(longest):
    longest = word

print("Longest word:", longest)