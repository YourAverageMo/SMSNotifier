import pandas
import requests

# API_KEY = "insert api key here"
API_KEY = "insert api key here"
LAT = 32.21975922020592
LON = -110.86531247903224
PART = "current,minutely,daily,alerts"

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={PART}&appid={API_KEY}")
# response.raise_for_status()
# data = response.json()
# with open("weather_forecast.json", mode="w") as file:
#     file.write(f"{data}")

hourly_data = pandas.read_json("./weather_forecast.json").hourly

# for hour in range(0, 12):
#     id = hourly_data[hour]["weather"][0]["id"]
# the better way to do this same line of code is to use list slicing like below

is_rain = False
for hour in hourly_data[:12]:
    id = hour["weather"][0]["id"]
    if id < 700:
        is_rain = True
if is_rain:
    print("its ganna rain, be like rihanna and bring an umbrella")
else:
    print("no rain today! u must not live in washington!")

# the next part she uses twilio to send sms messages to your phone which is very straight forward but i dont want to make an account for that so im not ganna do it.
