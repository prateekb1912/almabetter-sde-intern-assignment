import requests
import os


API_KEY = os.environ.get('WEATHERAPI_KEY')

def get_and_parse_weather_data(lon, lat):

    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')

    data = resp.json()

    weather_main = data['weather'][0]['main']
    temperature = fahrenheit_to_celsius(data['main']['temp'])
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    cloudiness = data['clouds']['all']
    timezone = data['timezone']/3600
    city = data['name']

    res_data = {
        'weather': weather_main,
        'temp': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'cloudiness': cloudiness,
        'timezone': timezone,
        'city': city
    }

    return res_data

def fahrenheit_to_celsius(fahrenheit_temp):
    celsius = (fahrenheit_temp - 32) * (5/9)

    return float(f'{celsius:.2f}')