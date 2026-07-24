b=int(input("Enter the gender of Driver enter 1 if Male & 2 if female"))
a=int(input("Enter maretial status , 3 if Married and 4 if not unmarried"))
c=int(input("Enter age of the driver"))

if a==3:
    print("The driver gets insurance")
elif b==1 and a==4 and c>30:
    print("The driver gets insurance")
elif a==4 and b==2 and c>25:
    print("Driver gets the insurance")