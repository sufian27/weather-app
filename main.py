import requests
import json

def main():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=71dc8342d714cc6d6a2e54b2eb8765a8"
    city = input("Enter city: ")
    r = requests.get(url.format(city))
    jsonfile = json.loads(r.text)
    while jsonfile["cod"] == "404": 
        print("City not found")
        city = input("Enter city: ")
        r = requests.get(url.format(city))
        jsonfile = json.loads(r.text)
    print('''
    Location: {}
    Weather: {}
    Current Temperature: {} C 
    Min Temperature: {} C
    Max Temperature {} C
    '''.format(city, jsonfile["weather"][0]["main"], jsonfile["main"]["temp"], jsonfile["main"]["temp_min"], 
    jsonfile["main"]["temp_max"]))

if __name__ == "__main__":
    main()