# Consider a program that asks for the age and, depending on the value received, returns a different message.
#  If the value is negative, it is an error.
#  If the value is between 0 and 17, it is a minor.
#  If the value is greater than or equal to 18, it is an adult.

age = int(input("Insert your age: "))

if age < 0:
    print("Error, the age should be greater than zero")
elif age < 18:
    print("You are a minor")
else:
    print("You are an adult")