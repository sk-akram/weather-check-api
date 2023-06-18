import requests

GEO_LOC_OWM_ENDPOINT= "http://api.openweathermap.org/geo/1.0/direct"
CURR_OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWM_API_KEY = "YOUR_API_KEY"#You can get it from OWM website after creating an account
#https://home.openweathermap.org/

city = input("Enter City Name: ").title()
geo_loc_params = {
    "q":city,
    "limit": 1,
    "appid": OWM_API_KEY
}


try:
    geo_response = requests.get(GEO_LOC_OWM_ENDPOINT, params=geo_loc_params)
    geo_response.raise_for_status()
    geo_loc_data = geo_response.json()
except Exception as e:
    print(e)
finally:
    city_lat = 22.5414185 #default
    city_lon = 88.35769124388872 #default

# print(geo_loc_data)
# print(len(geo_loc_data))

city_lat = geo_loc_data[0]['lat']
city_lon = geo_loc_data[0]['lon']

# print(city_lat, city_lon)

curr_weather_params = {
    "lat": city_lat,
    "lon": city_lon,
    "appid": OWM_API_KEY
}
try:
    curr_response = requests.get(CURR_OWN_ENDPOINT, params=curr_weather_params)
    curr_response.raise_for_status()
    curr_weather_data = curr_response.json()
    weather_data = curr_weather_data['weather']
    # print(curr_weather_data['weather'])
    print(f"Todays Weather in {city} : {weather_data[0]['main']}")

except Exception as e2:
    print(e2)


