#18.	Remove Duplicate Characters 
#Remove duplicate characters while maintaining the original order. 

str = input("Enter a string: ")

new_str = ""

for i in str:
    if i not in new_str:
        new_str = new_str + i

print("String after removing duplicates:", new_str)