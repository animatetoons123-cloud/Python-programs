# Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
str = input("Enter a string: ").lower()
vowels = 0
consonants = 0
digits =0
spaces =0
spch= 0
 
for i in str:
    if i in "aeiou":
        vowels +=1
    elif i in "bcdfghjklmnpqrstvwxyz":
        consonants +=1
    elif i in "0123456789":
        digits +=1
    elif i == " ":
        spaces +=1
    else:
        spch +=1
        
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", spch)
