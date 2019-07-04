from flask import Flask, render_template
from weather import get_weather
app = Flask(__name__)

@app.route("/")
def run():
    json_file_weather = get_weather()
    return render_template("index.html", location=json_file_weather["name"], 
    weather=json_file_weather["weather"][0]["main"], 
    temp_curr=json_file_weather["main"]["temp"], temp_min=json_file_weather["main"]["temp_min"], 
    temp_max=json_file_weather["main"]["temp_max"])

if __name__ == "__main__":
    app.run()