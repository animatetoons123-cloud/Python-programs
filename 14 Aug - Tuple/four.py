#Check whether color exists

colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter color: ")

if color in colors:
    print("Color exists")
else:
    print("Color does not exist")