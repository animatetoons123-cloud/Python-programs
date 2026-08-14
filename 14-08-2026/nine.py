#Check whether city exists

cities = ["Mumbai", "Pune", "Delhi", "Kolhapur", "Nashik"]

city = input("Enter city name: ")

if city in cities:
    print("City exists")
else:
    print("City does not exist")