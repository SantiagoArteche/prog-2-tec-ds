salaries_list = []

amount_of_salaries = int(input("Insert the amount of salaries: "))

init = 0
greater_than_twenty_five_thousand = 0
while(amount_of_salaries > init):
    salary = int(input("Insert your salary: "))
    salaries_list.append(salary)
    if(salary > 25000):
        greater_than_twenty_five_thousand += 1
    init += 1
salaries_list.sort()
print(f"Sorted list: {salaries_list} \n the amount of salaries greater than twenty five thousand is: {greater_than_twenty_five_thousand}")
