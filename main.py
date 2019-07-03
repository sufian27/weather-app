import requests
import json
from genkeys import generate_key

def main():

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
    ip_url = "http://api.ipstack.com/check?access_key={}"
    
    ###### ADD YOUR KEYS HERE, THE PROGRAM WON'T WORK WITHOUT IT #####
    weather_key = generate_key("weather")
    ip_key = generate_key("ip") 
    ##################################################################

    city = input("Enter city: ")
    r_weather = requests.get(weather_url.format(city, weather_key))
    json_file = json.loads(r_weather.text)
    while jsonfile["cod"] == "404": 
        print("City not found")
        city = input("Enter city: ")
        r = requests.get(weather_url.format(city, key))
        json_file = json.loads(r.text)
    print('''
    Location: {}
    Weather: {}
    Current Temperature: {} C 
    Min Temperature: {} C
    Max Temperature {} C
    '''.format(city, json_file["weather"][0]["main"], json_file["main"]["temp"], json_file["main"]["temp_min"], 
    json_file["main"]["temp_max"]))

if __name__ == "__main__":
    main()