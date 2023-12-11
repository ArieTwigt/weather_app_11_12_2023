from weather_functions.import_functions import import_weather_by_city


if __name__ == "__main__":

    # get the name of the city
    city_names = input("Insert a city:\n")

    # split to a list
    city_names_list = city_names.split(" ")

    # import the weather data of the city
    weather_list = import_weather_by_city(city_names_list)

    pass