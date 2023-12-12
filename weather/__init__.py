from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

# constant open weather map endpoint for weather data
OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
APPID = os.environ.get("APPID")

# check if there is a 'data' folder
if not os.path.exists("data"):
    os.mkdir("data")


class WeatherPrediction:


    def __init__(self, city):
        self.city = city

 