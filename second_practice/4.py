day = int(input("Insert the day of the week: "))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day < 1 or day > 7:
    print("The day number is between 1 and 7")
else:
    print(f"Today is: {week[day]}")