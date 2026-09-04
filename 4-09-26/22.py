# Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for n in numbers:
        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

        total = total + n

    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)
