countries = []
populations = []

amount_of_countries = int(input("Insert the amount of countries: "))

init = 0
while(init < amount_of_countries):
    country = input("Insert the country: ")
    population = int(input("Insert the population of the country: "))
    countries.append(country)
    populations.append(population)
    init += 1

references = {}

for index in range(len(countries)):
    references[populations[index]] = countries[index]

populations.sort(reverse=True)

sorted_countries = []
for population in populations:
    sorted_country = references.get(population)
    sorted_countries.append(sorted_country)

print(f"List of countries: {sorted_countries}")