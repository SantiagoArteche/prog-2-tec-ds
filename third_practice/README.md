# Exercise 1

### Code a Python function that calculates and prints the average of three grades.

### The grades are received as a parameter, and the average should be returned and displayed in the program that called the function.

# Exercise 2

### Develop a program that allows you to enter the side of a square. Then ask if you want to calculate and display its perimeter or its area, and based on that, call the perimeter or

### area function. Return the calculated value.

# Exercise 3

### Create a program using functions that allow you to manage folders and files. Call the corresponding function based on the selected function.

# Exercise 4

### Make a Fibonacci number generator

# Exercise 5

### Create a class called Person with private attributes: name, age, ID, sex (use an enumeration, see EnumGuerreros.py for an example), weight, and height.

### Create methods (getters and setters) to access and modify all attributes. By default, all attributes except the ID will have default values ​​based on their type

### (0 numbers, empty string for String, etc.). Sex will be female by default.

### calculateIMC(): calculates the person's body mass index (weight in kg/(height^2 in m))

### value_weight() returns -1 if the person is under their ideal weight, 0 if they are at their ideal weight, and 1 if they are overweight. Overweight is defined as a BMI > 25, and a person is considered underweight if a BMI < 18.

### is_adult(): indicates whether the person is of legal age, returns a boolean.

### **str**() returns all the person's information as a string of characters.

### generateID(): Generates a random 8-digit number that will be the person's ID.

### This method will not be visible from the outside. This method must be called from any constructor to generate the ID.

### Set and get methods for each parameter, except for ID, which will only have a get value.

### Now, create an executable class that does the following:

### Request the name, age, sex, weight, and height from the keyboard.

### Create 3 objects of the previous class. The first object will receive the previous variables requested from the keyboard. The second object will receive all of the previous variables except weight and height, and the last one will receive the default values. For the latter, use the set methods to assign a value to the attributes. For each object, you must check whether it is at its ideal weight, overweight, or underweight with a message.

### Indicate for each object whether it is of legal age.

### Finally, display the information for each object.
