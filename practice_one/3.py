age = int(input("Insert your age: "))

if age < 0:
    print("Error, the age should be greater than zero")
elif age < 18:
    print("You are a minor")
else:
    print("You are an adult")