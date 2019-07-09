from flask import Flask, render_template, request
from weather import get_weather
app = Flask(__name__)

@app.route("/")
def index():     
    return render_template("index.html")

@app.route("/weather", methods=["GET", "POST"])
def render_weather():
    #When the JS code sends the data to this page via POST, 
    #then the user latitude and longitude are stored in global variables
    if request.method == "POST":
        global my_lat
        global my_long 
        my_lat = request.form["latitude"]
        my_long = request.form["longitude"]
        return request.data
    #When the page is loaded via a GET request, then the page is rendered
    elif request.method == "GET":
        json_file_weather = get_weather(my_lat, my_long)    
        return render_template("weather.html", location=json_file_weather["name"], 
        weather=json_file_weather["weather"][0]["description"], 
        temp_curr=json_file_weather["main"]["temp"], temp_min=json_file_weather["main"]["temp_min"], 
        temp_max=json_file_weather["main"]["temp_max"])

if __name__ == "__main__":
    app.run()