# Enter a person's salary. If it exceeds $30,000, a message will appear on the screen
# indicating that taxes must be paid.

salary = int(input("Insert your salary: "))

if salary > 30000:
    print("Taxes must be paid")
