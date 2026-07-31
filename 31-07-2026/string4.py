#Check whether the entered string is a palindrome. 
str = input("Enter a string: ").lower()
reversed_str = str[::-1]
if str == reversed_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")