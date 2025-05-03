name = input("Insert your name: ")
password = str(input("Insert your password: "))

if(len(name) > 12 or len(name) < 6):
    print("The name should have between 6 and 12 characters")
elif(len(password) < 8):
    print("The password should have at least 8 characters")
elif(" " in password):
    print("The password musn't have blank spaces")
else:
    print(f"Success, welcome {name}")