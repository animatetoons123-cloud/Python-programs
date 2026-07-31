#16.	Character Frequency 
#	Display the frequency of every character in a string.
str = input("Enter a string: ")

for i in range(len(str)):
    count = 0

    for j in str:
        if str[i] == j:
            count = count + 1

    found = False

    for k in range(i):
        if str[i] == str[k]:
            found = True
            break

    if found == False:
        print(str[i], ":", count)