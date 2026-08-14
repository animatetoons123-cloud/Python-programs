#Sort 10 numbers ascending and descending

numbers = []

for i in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)