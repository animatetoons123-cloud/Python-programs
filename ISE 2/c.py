marks = []
total = 0

for i in range(5):
    m = int(input("Enter marks in subject: "))
    marks.append(m)

total = sum(marks)
percentage = total / 500 * 100

print("Total marks:", total)
print("Percentage:", percentage, "%")
