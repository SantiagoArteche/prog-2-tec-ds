numbers = []

number = 1
while(number != 0):
    number = int(input("Insert a number: "))
    if number != 0:
        numbers.append(number)

print(f"The length of the array is: {len(numbers)}")