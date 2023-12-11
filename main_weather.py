from weather_functions.import_functions import import_weather_by_city
from weather_functions.conversion_functions import convert_list_to_df

if __name__ == "__main__":

    # get the name of the city
    city_names = input("Insert a city:\n")

    # split to a list
    city_names_list = city_names.split(" ")

    # import the weather data of the city
    weather_list = import_weather_by_city(city_names_list)

    # convert to pandas DataFrames
    weather_df = convert_list_to_df(weather_list)

    # export to csv
    weather_df.to_csv("export.csv")

    pass