#  Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    return bill

units = int(input("Enter units consumed: "))

print("Electricity Bill:", electricity_bill(units))
