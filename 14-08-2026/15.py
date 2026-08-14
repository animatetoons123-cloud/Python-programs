#Find second largest element

numbers = [10, 40, 20, 50, 30]

numbers = list(set(numbers))
numbers.sort()

print("Second largest:", numbers[-2])