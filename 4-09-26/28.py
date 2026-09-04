# Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.

products = []

def add_product(name, price, quantity):
    products.append([name, price, quantity])

def remove_product(name):
    for product in products:
        if product[0] == name:
            products.remove(product)

def subtotal():
    total = 0

    for product in products:
        total = total + product[1] * product[2]

    return total

def coupon_discount(amount):
    return amount * 0.10

def gst(amount):
    return amount * 0.18

def invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)

    return taxable + tax

add_product("Pen", 20, 5)
add_product("Bag", 1000, 2)

print("Subtotal:", subtotal())
print("Final Invoice:", invoice())
