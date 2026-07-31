#Print all duplicate characters in a string. 

str = input("Enter a string: ")

print("Duplicate characters are:")

for i in range(len(str)):
    count = 0
    for j in range(len(str)):
        if str[i] == str[j]:
            count = count + 1

    if count > 1:
        print(str[i])