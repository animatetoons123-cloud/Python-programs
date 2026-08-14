#Merge two list
list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))

for i in range(n1):
    list1.append(int(input("Enter number: ")))

n2 = int(input("Enter number of elements in second list: "))

for i in range(n2):
    list2.append(int(input("Enter number: ")))

merged = list1 + list2

print("Merged list:", merged)