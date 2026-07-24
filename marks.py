n=int(input("Enter percentage of the student :"))

if n>=90 and n<100 :
    print("Excellent performance")
elif n<90 and n>=80 :
    print("Very good")
elif n<80 and n>=70 :
    print("Good performance")
elif n<70 and n>=60 :
    print("Average performance")
else :
    print("Poor performance")