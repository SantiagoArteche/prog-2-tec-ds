def side_of_the_square(side):
    question = int(input("What dou you want to know?\n1 - Perimeter\n2 - Surface\n"))

    if question == 1:
        surface = calculate_surface(side) 
        print(f"The surface of the square is {surface}")
    elif question == 2:
        perimeter = calculate_perimeter(side) 
        print(f"The perimeter of the square is {perimeter}")
    else:
        print("Incorrect value")
        side_of_the_square(side)

def calculate_perimeter(side):
    return side * 4

def calculate_surface(side):
    return side * side

side_of_the_square(7)
