# Create a function to find the second-largest number in a list.

def second_largest(numbers):
    unique = []

    for n in numbers:
        if n not in unique:
            unique.append(n)

    unique.sort()

    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(numbers))
