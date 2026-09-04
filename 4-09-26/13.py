# Write a function that accepts a list of numbers and returns their average.

def average(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total / len(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))

print("Average:", average(numbers))
