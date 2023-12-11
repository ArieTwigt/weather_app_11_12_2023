from weather_functions.import_functions import import_weather_by_city


if __name__ == "__main__":

    # get the name of the city
    city_name = input("Insert a city:\n")

    # import the weather data of the city
    weather_dict = import_weather_by_city()

    pass