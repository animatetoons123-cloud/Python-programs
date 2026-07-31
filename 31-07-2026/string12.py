#a.	Find the shortest word in a sentence. 

str = input("Enter a string: ")

word = ""
smallest = ""

for i in str:
    if i != " ":
        word = word + i
    else:
        if smallest == "" or len(word) < len(smallest):
            smallest = word
        word = ""


if smallest == "" or len(word) < len(smallest):
    smallest = word

print("Shortest word:", smallest)