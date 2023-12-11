from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

# constant open weather map endpoint for weather data
OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
APPID = os.environ.get("APPID")