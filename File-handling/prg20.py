file = open("transactions.txt", "r")

total_deposit = 0
total_withdrawal = 0
balance = 0
largest = 0

for line in file:
    data = line.strip().split(",")

    type = data[0]
    amount = int(data[1])

    if amount > largest:
        largest = amount

    if type == "D":
        total_deposit = total_deposit + amount
        balance = balance + amount

    elif type == "W":
        total_withdrawal = total_withdrawal + amount
        balance = balance - amount

file.close()

print("Total deposits:", total_deposit)
print("Total withdrawals:", total_withdrawal)
print("Final balance:", balance)
print("Largest transaction:", largest)