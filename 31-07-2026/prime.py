num = int(input("Enter a number: "))

i = 2
isPrime = True

if num <= 1:
    isPrime = False
else:
    while i < num:
        if num % i == 0:
            isPrime = False
            break
        i = i + 1

if isPrime:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")