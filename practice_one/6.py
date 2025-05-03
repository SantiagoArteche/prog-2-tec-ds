# 1
init = 0
sum = 0
iterations = 12
while(init < iterations):
    value = int(input("Insert a number: "))
    sum = sum + value
    init = init + 1

print(f"The sum of the values is: {sum} \n and the average: {round(sum / iterations)}")


# 2
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