n=int(input("Enter a number print sum of odd numbers upto - "))

i=1
sum=0
while i<n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Sum of odd no. is - ",sum)