#Accept five numbers and convert list into tuple
numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

numbers = tuple(numbers)

print(numbers)