import json
import requests


city = input("Give city name: ")
api_key = "9858b157b6ed6340b3fbebbb2a25e42d"
api_value = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"

lat = None
lon = None

response = requests.get(api_value)
if response.status_code == 200:
    locationdata = response.json()
    lat = locationdata[0]["lat"]
    lon = locationdata[0]["lon"]
    if lat is None and lon is None:
        print("Latitude and longitude not found")


if lat is not None or lon is not None:
    api_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    weatherresponse = requests.get(api_weather)
    if weatherresponse.status_code == 200:
        weatherdata = weatherresponse.json()
        temperature = weatherdata.get("main", {}).get("temp")
        description = weatherdata["weather"][0].get("description")
        if temperature and description:
            print(f"Weather: {description}")
            print(f"Temperature: {temperature-273.15:.2f} C")
        else:
            print("Weather request failed:", weatherresponse.status_code)

