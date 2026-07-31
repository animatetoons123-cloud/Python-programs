#a.	Check whether a given substring exists in the main string

str = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in str:
    print("Substring exists")
else:
    print("Substring does not exist")