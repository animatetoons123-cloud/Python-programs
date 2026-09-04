# Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def consultation_charge():
    return 500

def laboratory_charge():
    return 1000

def medicine_charge():
    return 1500

def room_charge(days):
    return days * 1000

def final_bill(days, category):
    total = consultation_charge() + laboratory_charge() + medicine_charge() + room_charge(days)

    if category == "senior":
        discount = total * 0.20
    elif category == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

days = int(input("Enter room days: "))
category = input("Enter patient category: ")

print("Final Bill:", final_bill(days, category))
