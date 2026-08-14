#Modify tuple using list

numbers = (10, 20, 30, 40, 50)

numbers = list(numbers)

position = int(input("Enter position to modify: "))
new_value = int(input("Enter new value: "))

numbers[position] = new_value

numbers = tuple(numbers)

print(numbers)