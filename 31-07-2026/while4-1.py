#Write a PYTHON program to print the multiplication table

number = int(input("Enter a number: "))     

i=1
while i <= 10:
    print(number, 'x', i, '=', number*i)
    i = i + 1
    
    