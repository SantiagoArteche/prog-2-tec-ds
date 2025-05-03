grade = int(input("Insert calification"))

greater_equal_than_seven = 0
less_than_seven = 0
while(grade != 0):
    if(grade >= 7):
        greater_equal_than_seven = greater_equal_than_seven + 1
    else:
        less_than_seven = less_than_seven + 1
    grade = int(input("Insert calification: "))

print(f"The number of students with califications greater equal than seven is: {greater_equal_than_seven} \n and the number with less than seven is: {less_than_seven}")