def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

avg = average([10, 2, 3])
print(f"The average of the califications is {avg}")
