#	Remove all spaces from the input string

str=input("Enter a string : ")
new_str=" "

for i in str:
    if i!=" ":
        new_str=new_str + i
        
print("New string without spaces",new_str)