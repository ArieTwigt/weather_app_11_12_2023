from typing import Dict, List
from weather_functions import OPEN_WEATHER_ENDPOINT, APPID
import requests


#def import_weather_by_city(*cities:str) -> List[Dict]:
def import_weather_by_city(cities: List, 
                           skip_on_error: bool=True) -> List[Dict]:
    """
    Function to import weather for a city

    Parameters:

    * city: City to return the weather from

    Returns:

    * A dictionary containing the weather information

    """
    ''' # voorbeeld voor checken types
    # check for the right type
    required_type = List

    if type(cities) != required_type:
        raise TypeError("Not the right type")
    '''


    # empty list with predictions
    predictions_list = []


    # loop for getting weather data
    for city in cities:

        # define the endpoint for importing the weather data
        endpoint = f"{OPEN_WEATHER_ENDPOINT}?q={city}&appid={APPID}&units=metric" 

        # execute the request
        response = requests.get(endpoint)

    
        # check if the response is valid
        if not (200 <= response.status_code < 299):
            if skip_on_error:
                print(f"No predictions for {city}")
                continue
            else:
                raise ValueError(f"No predictions for city: {city}")

        # get the data from the response
        weather_dict = response.json()

        # get the predictions from the data
        # specify the elements we want to retreive
        weather_temp        = []
        weather_feels_like  = []
        weather_rain_mm     = []
        weather_description = []
        weather_dt_txt      = []

        # loop for getting information
        for i in range(0, len(weather_dict['list'])):
            weather_temp.append(weather_dict['list'][i]['main']['temp'])  
            weather_feels_like.append(weather_dict['list'][i]['main']['feels_like'])
            if "rain" in weather_dict['list'][i].keys():
                weather_rain_mm.append(weather_dict['list'][i]['rain']['3h'])
            else:
                weather_rain_mm.append(0)  
            weather_description.append(weather_dict['list'][i]['weather'][0]['description'])
            weather_dt_txt.append(weather_dict['list'][i]['dt_txt'])
        
        
        # create a new dictionary with a dict-comprehension
        weather_dict_clean = {# structure
                            dt: {
                                "temperature": temperature,
                                "feels_like": feels_like,
                                "rain": rain,
                                "description": description,
                                "city": city
                            }
                            # vars
                            for temperature, feels_like, rain, description, dt
                            # iterables
                            in zip(weather_temp, weather_feels_like, weather_rain_mm,
                            weather_description, weather_dt_txt)

                                    }
        
        # add the dictionary to the predictions list
        predictions_list.append(weather_dict_clean)

    
    return predictions_list

