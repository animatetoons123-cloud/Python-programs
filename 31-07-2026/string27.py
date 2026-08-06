#27. Email Validator


email = input("Enter an email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")