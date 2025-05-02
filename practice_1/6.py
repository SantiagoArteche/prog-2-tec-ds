# Develop a program that allows you to enter 12 values ​​from the keyboard and then displays the sum of the entered values ​​and their average. 
# The result of the average is a real value, i.e., with a comma. 
# If you want the division result to return only the integer portion of the average, you must use the operator


init = 0
sum = 0
iterations = 12
while(init < iterations):
    value = int(input("Insert a number: "))
    sum = sum + value
    init = init + 1

print(f"The sum of the values is: {sum} \n and the average: {round(sum / iterations)}")

# Develop a program that allows us to enter 10 numbers and tell us whether each number is even or odd.

init = 0
iterations = 10
results = []
while(init < iterations):
    value = int(input("Insert a number: "))
    is_even = value % 2 == 0
    results.append([value, is_even])
    init = init + 1

for result in results:
    value = result[0]
    is_even = result[1]
    if(is_even):
        print(f"{value} - is even")
    else:
        print(f"{value} - is odd")