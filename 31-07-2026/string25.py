#25. Second Most Frequent Character



s = input("Enter a string : ")

first = ""
second = ""

for ch in set(s):
    if first == "" or s.count(ch) > s.count(first):
        second = first
        first = ch
    elif second == "" or s.count(ch) > s.count(second):
        if ch != first:
            second = ch

print(second)