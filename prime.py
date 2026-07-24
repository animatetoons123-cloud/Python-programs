#prog to check entered no is prime or not 

n=int(input("Enter a number to check if its prime or not :"))

i = 2

while i < n:
    if n % i == 0:
        print(n, "is not Prime Number")
        break
    i = i + 1
else:
    print(n, "is a Prime Number")