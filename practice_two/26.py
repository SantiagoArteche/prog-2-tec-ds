
def load_four_people():
    dictionary = {}
    amount_of_people = 4
    for _ in range(amount_of_people):
        document_number = input("Insert your document number: ")
        name = input("Insert your name: ")
        dictionary[document_number] = name
    return dictionary

def people_list(dictionary: dict):
    print("People list: ")
    for document_number, name in dictionary.items():
        print_info(document_number, name)

def find_person(document_number: str, dictionary: dict):
    if(dictionary.get(document_number)):
        name = dictionary.get(document_number)
        print_info(document_number, name)
    else:
        print(f"The person with the document number: {document_number} was not found")
    
def print_info(document_number: str, name: str):
    print(f"Document number: {document_number}. Name: {name}")

dictionary = load_four_people()
people_list(dictionary)

document_number = input("Insert the document number of the person: ")
find_person(document_number, dictionary)