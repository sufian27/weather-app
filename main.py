import requests
import json
from genkeys import generate_key

def main():

    weather_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&APPID={}"
    ip_url = "http://api.ipstack.com/check?access_key={}"
    
    ###### ADD YOUR KEYS HERE, THE PROGRAM WON'T WORK WITHOUT IT #####
    weather_key = generate_key("weather")
    ip_key = generate_key("ip") 
    ##################################################################

    r_ip = requests.get(ip_url.format(ip_key))
    json_file_ip = json.loads(r_ip.text)
    user_lat = json_file_ip["latitude"]
    user_long = json_file_ip["longitude"]
    r_weather = requests.get(weather_url.format(user_lat, user_long, weather_key))
    json_file_weather = json.loads(r_weather.text)
    if json_file_weather["cod"] == "404": 
        print("Location not found")
    else: 
        print('''
        Your Location: {}
        Weather: {}
        Current Temperature: {} C 
        Min Temperature: {} C
        Max Temperature {} C
        '''.format(json_file_weather["name"], json_file_weather["weather"][0]["main"], json_file_weather["main"]["temp"], 
        json_file_weather["main"]["temp_min"], json_file_weather["main"]["temp_max"]))

if __name__ == "__main__":
    main()