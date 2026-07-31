#Replace all occurrences of a given character with another character. 

str=input("Enter a string : ")
ch=input("Enter letter to replace :")
new=input("Enter new letter to replace with :")

updated=" "
for i in str:
    if i==ch:
        updated=updated+new
    else:
        updated = updated + i

print("updated string: ",updated)