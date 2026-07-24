x=int(input("Enter first number :"))
y=int(input("Enter second number :"))
z=int(input("Enter third number :"))

if x>y and x>z :
    print("The First number", x,"is largest" )
elif y>x and y>z:
    print("The second number", y,"is largest")
else:
    print("The third number", z, "is largest")