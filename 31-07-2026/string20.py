#21.	Password Validator
#	Validate a password based on these conditions: 
#	Minimum 8 characters 
#	At least one uppercase letter 
#	One lowercase letter 
#	One digit 
#	One special character

password = input("Enter a password: ")

upper = 0
lower = 0
digit = 0
special = 0

for i in password:
    if i.isupper():
        upper = upper + 1
    elif i.islower():
        lower = lower + 1
    elif i.isdigit():
        digit = digit + 1
    else:
        special = special + 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")