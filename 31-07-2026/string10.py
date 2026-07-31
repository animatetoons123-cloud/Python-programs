#11.	Word Count 
#	Count the total number of words in a sentence. 

str=input("Enter a string : ")
count=0

for i in str:
    if i == " ":
        count = count + 1

print("Total number of words:", count +1)