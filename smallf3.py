x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=int(input("Enter third number :"))

if x<y and x<z :
    print("The First number", x,"is smallest" )
elif y<x and y<z:
    print("The second number", y,"is smallest")
else:
    print("The third number", z, "is smallest")