# A number from 1 to 7 must be entered and, depending on the number entered, the day of the week to which it corresponds is displayed. # 1 is Sunday.

day = int(input("Insert the day of the week: "))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day < 1 or day > 7:
    print("The day number si between 1 and 7")
else:
    print(f"Today is: {week[day]}")