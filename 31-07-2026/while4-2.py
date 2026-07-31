#Write a PYTHON program to print the largest of n numbers

n = int(input("Enter the number of elements: "))
first = int(input("Enter the first number: "))

i = 1
while i < n:
    num = int(input("Enter the next number: "))
    if num > first:
        first = num
    i = i + 1

print("The largest number is", first)