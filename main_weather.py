from weather.weather import WeatherPrediction
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

    # initiate a WeatherPrediction instance
    prediction = WeatherPrediction(cities)

    # call the method to generate predictions
    prediction.import_weather_by_city()

    # convert the predictions to a DataFrame
    prediction.convert_list_to_df()


    if export_type == "csv":
    # export the DataFrame
        prediction.export_data(export_name)
    else:
        print(prediction.show_predictions_df())
