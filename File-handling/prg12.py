file = open("student.txt", "r")

data = file.read().lower()
words = data.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

file.close()

print("Word frequency:")
print(frequency)