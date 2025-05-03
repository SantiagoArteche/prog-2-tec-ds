def set_grade(name, grade, very_good_amount):
    if grade >= 8:
        califications.append([name, grade, "Very Good"])
        very_good_amount += 1
    elif grade >= 4:
        califications.append([name, grade, "Good"])
    else:
        califications.append([name, grade, "Insufficient"])
    
    return very_good_amount

amount_of_students = int(input("Insert the amount of students: "))

init = 0

califications = []
very_good_amount = 0
while amount_of_students > init:
    name = input("Insert the name of the student: ")
    grade = int(input("Insert the grade of the student: "))
    very_good_amount = set_grade(name, grade, very_good_amount)   
    init += 1

print(f"List of califications: {califications} \n amount of very good grades: {very_good_amount}")



    