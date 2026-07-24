n=int(input("Enter year to check if year is Leap or not : "))

if (n%4==0 and n%100!=0) or n%400==0:
    print("Entered year is leap")
else:
    print("Year is not leap")