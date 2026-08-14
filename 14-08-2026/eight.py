#Count even and odd numbers

numbers = []

for i in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)