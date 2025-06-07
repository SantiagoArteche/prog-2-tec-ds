phrase = input("Enter the phrase: ")

print(f"The list made from the phrase is: {phrase.split()}")

phrase_list = []
string_builder = ""
for char in phrase:
    string_builder += char
    if(char == " " or char == phrase[-1]):
        phrase_list.append(string_builder.strip())
        string_builder = ""
        

print(f"The list made from the phrase is: {phrase_list}")