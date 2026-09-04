# Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = list(map(int, input("Enter 5 marks: ").split()))

    total = total_marks(marks)
    percent = percentage(marks)
    g = grade(percent)

    students.append([name, roll, marks, total, percent, g])

for student in students:
    print(student[0], student[1], student[3], student[4], student[5])

class_average = sum(student[4] for student in students) / n
highest = max(students, key=lambda x: x[4])
lowest = min(students, key=lambda x: x[4])

print("Class Average:", class_average)
print("Highest Scorer:", highest[0])
print("Lowest Scorer:", lowest[0])
