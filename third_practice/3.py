import os

message = "What do you want to do?\n1- Read a file\n2- Create a file\n3- Overwrite a file\n4- Add information to a file\n5- Delete a file\n"
try:
    question = int(input(message))
except:
    print("Invalid type")
def options(value):
    valid_values = [1,2,3,4,5]
    if(value in valid_values):
        file_name = input("Insert the file name: ")
        file_with_format = file_name + '.txt'
        file_not_found_message = "File not found"
        file_modified_message = "File modified, new data: "
        new_data_message = "New data: "

        if value == 1:
            try:
                file = open(f"./{file_with_format}", 'r')
                print(file.read())
            except:
                print(file_not_found_message)
        elif value == 2:
            try:
                open(f"./{file_with_format}", 'x')
                print("File created")
            except:
                print("The file exists")
        elif value == 3:
            new_data = input(new_data_message)
            file = open(f"./{file_with_format}", 'w+')
            file.write(new_data)
            file.seek(0)
            print(file_modified_message)
            print(file.read())
        elif value == 4:
            new_data = input(new_data_message)
            file = open(f"./{file_with_format}", 'a+')
            file.write(f"\n{new_data}")
            print(file_modified_message)
            file.seek(0)
            print(file.read())
        elif value == 5:
            try:
                os.remove(file_with_format)
            except:
                print(file_not_found_message)
    else:
        error_message = "\nIncorrect value, try again"
        print(error_message)
        try:
            question = int(input(message))
            options(question)
        except:
            print(error_message)
            question = int(input(message))
            options(question)


options(question)

