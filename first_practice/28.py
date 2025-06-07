def load_data(amount_of_countries: int):
    init = 0
    countries = {}
    while(init < amount_of_countries):
        country_name = input("Insert the name of the country: ")
        media_temperature_amount = 3
        media_temperatures = []
        for index in range(media_temperature_amount):
            media_temperature = float(input(f"Insert the {get_ordinal_word(index + 1)} media temperature: "))
            media_temperatures.append(media_temperature)
        countries[country_name] = media_temperatures
        init += 1
    return countries

def print_data(countries: dict):
    for name, temperatures in countries.items():
        print(f"The name of the country is: {name}")
        for index in range(len(temperatures)):
            print(f"The {get_ordinal_word(index + 1)} media temperature is: {temperatures[index]}")

def trimestral_average_temperature(countries: dict):
    trimestral_dictionary = {}
    for name, temperatures in countries.items():
        trimestral_dictionary[name] = sum(temperatures) / len(temperatures)
    return trimestral_dictionary

def print_trimestral_data(countries: dict):
    for name, avg_temperature in countries.items():
        print(f"The name of the country is: {name} and his average temperature is: {avg_temperature}")

def get_max_trimestral_temperature(countries: dict):
    max_value = float('-inf')
    country_max_trimestral = []
    for name, temperature in countries.items():
        if(temperature > max_value):
            max_value = temperature
            country_max_trimestral = [name, temperature]
    return country_max_trimestral

def get_ordinal_word(number: int):
    ordinal_word = ''
    if number == 1:
        ordinal_word = "first"
    elif number == 2:
        ordinal_word = "second"
    else:
        ordinal_word = "third"
    return ordinal_word

amount_of_countries = int(input("Insert the amount of countries: "))
countries = load_data(amount_of_countries)
print("")
print_data(countries)
print("")
trimestral_average = trimestral_average_temperature(countries)
print_trimestral_data(trimestral_average)
print("")
country_max_trimestral = get_max_trimestral_temperature(trimestral_average)
print(f"The country with the max trimestral average is: {country_max_trimestral[0]}, and the his is: {country_max_trimestral[1]}")
