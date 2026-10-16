file = open("student.txt", "a")

name = input("Enter another student name: ")
roll = input("Enter roll number: ")

file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")

file.close()

print("Information added successfully.")