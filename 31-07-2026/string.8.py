# Find the number of times a specified character appears in a string. 
str=input("Enter a string : ")

ch=input("Enter character to count its frequency :")
count=0
for i in str:
    if i==ch:
        count+=1
        

print("Number of character ",ch," appeared in string is ",count)