sentence = input("Insert your sentence: ")

blank_spaces = 0
for char in sentence:
    if char == " ":
        blank_spaces += 1

print(f"The number of blank spaces is: {blank_spaces}")

