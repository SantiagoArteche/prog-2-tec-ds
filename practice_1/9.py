# A company has n employees whose salaries range between $100 and $500. 
# Create a program that reads the salaries of each employee and reports how many employees earn between $100 and $300 and how many earn more than $300. 
# The program must also report the amount the company spends on staff salaries.

number_of_employees = int(input("Insert number of employees: "))
init = 0
total_amount = 0
between_three_hundred_and_one_hundred = 0
greater_than_three_hundred = 0
error = False
while(number_of_employees > init):
    salary = int(input("Insert the salary: "))
    if(salary > 500 or salary < 100):
        error = True
        break
    elif(salary <= 300 and salary >= 100):
        between_three_hundred_and_one_hundred = between_three_hundred_and_one_hundred + 1
    else:
        greater_than_three_hundred = greater_than_three_hundred + 1
    total_amount = total_amount + salary
    init = init + 1

if(error):
    print("Bad input, try again. The numbers should be greater equal than 100 and less equal than 500")
else:
    print(f"The number of employees which salary is between $100 and $300 is: {between_three_hundred_and_one_hundred} \n the number of employees which salary is greater than $300 is: {greater_than_three_hundred} \n amount expend in personnel salary: ${total_amount}")