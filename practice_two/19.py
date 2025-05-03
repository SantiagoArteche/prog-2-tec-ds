cities = []

cities_amount = int(input("Insert the amount of cities: "))

init = 0

while(cities_amount > init):
    city = input("Insert the name of the city: ")
    cities.append(city)
    init += 1

city_name = input("Insert the name of the city are you looking for: ")

if(not city_name in cities):
    print("We can't found the city")
else:
    for index in range(len(cities)):
        if(cities[index] == city_name):
            print(f"The index of the city is: {index}")
            break