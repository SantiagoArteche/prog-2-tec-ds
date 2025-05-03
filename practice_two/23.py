number_of_employees = 5

salaries = {}

init = 0
while(init < number_of_employees):
    name = input("Insert the name of the employee: ")
    salary1 = int(input("Insert the salary: "))
    salary2 = int(input("Insert the second salary: "))
    salary3 = int(input("Insert the third salary: "))
    salaries[name] = (salary1, salary2, salary3)
    init += 1

for key, value in salaries.items():
    make_response = f"Employee: {key} \n"
    iteration = 0
    for val in value:
        iteration += 1
        make_response += f"Salary {iteration} = {val}"
    print(make_response)