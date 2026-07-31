#	Count the number of uppercase and lowercase letters in a string
str=input("Enter a string : ")

uppercase=0
lowercase=0

for i in str:
    if i.isupper():
        uppercase+=1
    
    elif i.islower():
        lowercase+=1
        
print("Number of uppercase char in string : ",uppercase)
print("Number of lowercase char in string : ",lowercase)