file = open("student.txt", "r")

lines = file.readlines()

file.close()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line, end="")