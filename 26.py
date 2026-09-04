# Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_units(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5

def fixed_charge():
    return 100

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount):
    if amount > 2000:
        return amount * 0.10
    return 0

def final_bill(units):
    amount = calculate_units(units)
    amount = amount + fixed_charge()
    tax = calculate_tax(amount)
    discount = calculate_discount(amount)

    return amount + tax - discount

units = int(input("Enter units: "))

print("Final Bill:", final_bill(units))
