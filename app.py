from flask import Flask, render_template, request
from weather import get_weather
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    json_file_weather = get_weather()
    if request.method == "POST": 
        print(request.form["latitude"])
        print(request.form["longitude"])
    return render_template("index.html", location=json_file_weather["name"], 
    weather=json_file_weather["weather"][0]["description"], 
    temp_curr=json_file_weather["main"]["temp"], temp_min=json_file_weather["main"]["temp_min"], 
    temp_max=json_file_weather["main"]["temp_max"])

if __name__ == "__main__":
    app.run()