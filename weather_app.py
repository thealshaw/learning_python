import requests
import json
from datetime import date
from geopy.geocoders import Nominatim

## select a city you want to know the weather forcast for
city = input("Enter City Name\n")

## we calculate the coordanets for that city 
geolocator = Nominatim(user_agent="geoapiExercises")

def get_location(city):
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)
lati , long = get_location(city)

## we request the information from the API 
url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"

querystring = {"lat":str(lati),"lon":str(long),"timezone":"auto","language":"en","units":"auto"}

headers = {
	"X-RapidAPI-Key": "cfdefcca40msh16e68377b42e119p16528bjsn871851f3c325",
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
dt = date.today()
data = response.text
js = json.loads(data)
#print(json.dumps(js, indent=4))

# we print the information
print("Weather in", city, "today", dt, "is", js["current"]["summary"])
print("temperature is", js["current"]["temperature"])
print("feels like", js["current"]["feels_like"])
print("wind speed", js["current"]["wind"]["speed"], "km/h")
print("precipitation is at", js["current"]["precipitation"]["total"], "mm")
print("humidity is at", js["current"]["humidity"], "%")
