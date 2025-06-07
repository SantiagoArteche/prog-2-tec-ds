

from random import randint
from enum import Enum

class Persona:
    SEX_ENUM = Enum('sex', ['female', 'male'])
    def __init__(self, name = '', age = 0, sex = SEX_ENUM.female, weight = 0, height = 0):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__dni = self.__generate_id()
        self.__weight = weight
        self.__height = height

    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nDNI: {self.__dni}\nSex: {self.__sex}\nWeight: {self.__weight}kg\nHeight: {self.__height}m"
    
    def __generate_id(self):
        dni = ''
        while(len(dni) < 8):
            dni += f"{randint(0,9)}"
        return dni

    def is_adult(self):
        return self.__age >= 18

    def calculate_imc(self):
        if(self.__height <= 0):
            return "Invalid values"
        return self.__weight / (self.__height ** 2)
    
    def value_weight(self):
        imc = self.calculate_imc()
        if(isinstance(imc, str)):
            return -2
        elif(imc < 18.5):
            return -1
        elif(imc < 25):
            return 0
        else:
            return 1
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    def get_age(self):
        return self.__age
    
    def set_age(self, value):
        self.__age = value
    
    def get_dni(self):
        return self.__dni
    
    def get_sex(self):
        return self.__sex
    
    def set_sex(self, value):
        self.__sex = value
    
    def get_weight(self):
        return self.__weight
    
    def set_weight(self, value):
        self.__weight = value

    def get_height(self):
        return self.__height
    
    def set_height(self, value):
        self.__height = value

class Executable(Persona):
    def __init__(self, name='', age=0, sex = '', weight=0, height=0):
        person = Persona(name, age, sex, weight, height)
        person1 = Persona(name, age, sex)
        person2 = Persona()
        person2.set_name("Valentin")
        person2.set_age(13)
        person2.set_sex("male")
        person2.set_weight(45)
        person2.set_height(170)
        print()
        print(self.weight_condition(person))
        print()
        print(self.weight_condition(person1))
        print()
        print(self.weight_condition(person2))
        print()
        print(self.is_adult(person))
        print()
        print(self.is_adult(person1))
        print()
        print(self.is_adult(person2))
        print()
        print(person)
        print()
        print(person1)
        print()
        print(person2)

        
    def weight_condition(self, instance: Persona):
        if(instance.value_weight() == -1):
            return f"{instance.get_name()} is below his ideal weight"
        elif(instance.value_weight() == 0):
            return f"{instance.get_name()} is on his ideal weight"
        elif(instance.value_weight() == -2):
            return f"{instance.get_name()} has incalculable parameters"
        else:
            return f"{instance.get_name()} has overweight"

    def is_adult(self, instance: Persona):
        if(instance.is_adult()):
            return f"{instance.get_name()} is adult"
        else:
            return f"{instance.get_name()} is child"
        
        
        
name = input("Insert your name: ")
hasError = False
try:
    age = int(input("Insert your age: "))
    weight = float(input("Insert your weight in kilograms: "))
    height = float(input("Insert your height in meters: "))
except:
    hasError = True
    print("The field must be an integer")


if not hasError:
    sex = input("Insert your sex - (Male - Female): ")

    if sex.lower() not in ('male', "female"):
        print("Incorrect sex")
    else:
        Executable(name, age, sex.lower(), weight, height)

