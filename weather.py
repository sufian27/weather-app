import requests
import json
from genkeys import generate_key

def get_weather(my_lat, my_long):
    weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&APPID={}"
    
    ###### ADD YOUR KEY HERE, THE PROGRAM WON'T WORK WITHOUT IT #####
    weather_key = generate_key()
    ##################################################################

    r_weather = requests.get(weather_url.format(my_lat, my_long, weather_key))
    json_file_weather = json.loads(r_weather.text)
    return json_file_weather
