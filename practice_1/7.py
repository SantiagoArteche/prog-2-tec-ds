# A job applicant takes a training test and obtains the following information:
# Total number of questions asked and the number of questions answered
# correctly. A program is required to create a program that enters both data points using the keyboard and reports the applicant's
# level based on the percentage of correct answers obtained, knowing that:
# Maximum level: Percentage >=90%.
# Average level: Percentage >=75% and <90%.
# Regular level: Percentage >=50% and <75%.
# Below level: Percentage <50%.

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