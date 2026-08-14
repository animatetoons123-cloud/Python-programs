#Accept 10 numbers and calculate sum and average

numbers = []

for i in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

total = sum(numbers)
average = total / 10

print("Sum:", total)
print("Average:", average)