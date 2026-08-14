#Convert tuple into list and add element

numbers = (10, 20, 30, 40, 50)

numbers_list = list(numbers)

new_number = int(input("Enter new number: "))
numbers_list.append(new_number)

print(numbers_list)