

total_answers = int(input("Insert total answers amount: "))
correct_answers = int(input("Insert correct answrs amount: "))

percentage = (correct_answers / total_answers) * 100

if(percentage >= 90):
    print("Maximum level")
elif(percentage >= 75):
    print("Average level")
elif(percentage >= 50):
    print("Regular level")
else:
    print("Below level")