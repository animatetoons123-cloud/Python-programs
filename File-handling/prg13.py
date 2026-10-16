file = open("student.txt", "r")

word = input("Enter word to search: ")

count = 0
line_number = 0

for line in file:
    line_number = line_number + 1
    words = line.split()

    for w in words:
        if w.lower() == word.lower():
            count = count + 1
            print("Found in line:", line_number)

file.close()

print("Total occurrences:", count)