#Reverse the given string without using built-in reverse functions. 
str = input("Enter a string: ")
reversed_str = ""
for i in str:
    reversed_str = i + reversed_str
print("Reversed string:", reversed_str)

# every new letter gets added and another gets addes in front of it using for loop