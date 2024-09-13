import requests

latitude ="37.21"
longitude ="-93.30"


#print("Forecast for the next few days:")
print("Current weather: \n")

base_url ="https://api.weather.gov/" 
grid_points = requests.get(base_url +"points/"+latitude +","+longitude)

#print(grid_points.json())

forecast = requests.get(grid_points.json()["properties"]["forecast"])

hourly_fc = requests.get(grid_points.json()["properties"]["forecastHourly"])

current_weather = hourly_fc.json()["properties"]["periods"][0]

print ("Temperature: "+ str(current_weather["temperature"]) + "\nRelative humidity: " + str(current_weather["relativeHumidity"]["value"]) + "\nWind Speed: "+ str(current_weather["windSpeed"]) + "\nDirection: " + current_weather["windDirection"])

full_forecast = forecast.json()["properties"]["periods"]

print("Next Three Days: \n")
for day in range(5):
    print(full_forecast[day]["name"])
    print(full_forecast[day]["detailedForecast"])

def detail_forecast():
    for day in range(len(full_forecast)):
        print(full_forecast[day]["name"])
        print(full_forecast[day]["detailedForecast"])
    
#def hourly_forecast():

