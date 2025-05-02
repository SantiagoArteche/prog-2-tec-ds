# Create a program that requests two different numbers and displays the highest number of them on the screen.

number_one, number_two = int(input("Insert number1: ")), int(input("Insert number2: "))

max_number = max(number_one, number_two)

print(f"The greatest number is: {max_number}")