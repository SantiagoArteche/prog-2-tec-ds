sentence = input("Insert your sentence: ")

vowels = ["a", "e", "i", "o", "u"]

vowel_counter = 0
for char in sentence:
    if char in vowels:
        vowel_counter += 1

print(f"The amount of vowels in the sentence is: {vowel_counter}")