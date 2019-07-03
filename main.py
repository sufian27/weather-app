import requests
import json

def main():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=71dc8342d714cc6d6a2e54b2eb8765a8"
    city = input("Enter city: ")
    r = requests.get(url.format(city))
    print(r.text)

if __name__ == "__main__":
    main()