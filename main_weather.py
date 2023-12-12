from weather_functions.import_functions import import_weather_by_city
from weather_functions.conversion_functions import convert_list_to_df
import argparse


# initiate the argument parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("--cities", "-c",
                    required=True,
                    help="Specify list of cities between quotes",
                    type=lambda s: [item.strip() for item in s.split(',')])

parser.add_argument("--export_type", "-e",
                    type=str,
                    choices=['csv', 'print'],
                    default='print')


parser.add_argument("--export_name", "-en",
                    type=str,
                    default="export",
                    required=False)

# parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    # get the arguments
    cities = args.cities
    export_type = args.export_type
    export_name = args.export_name


    # import the weather data of the city
    weather_list = import_weather_by_city(cities)

    # convert to pandas DataFrames
    weather_df = convert_list_to_df(weather_list)

    # based on the export
    if export_type == 'csv':
        print("Exporting to csv")
        weather_df.to_csv(f"{export_name}.csv",
                          index=False)
    else:
        print(weather_df)

    pass