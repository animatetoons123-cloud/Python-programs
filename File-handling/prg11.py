file = open("student.txt", "r")

data = file.read()

words = data.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

file.close()

print("Longest word:", longest)
print("Length:", len(longest))