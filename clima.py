import datetime as dt
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('weather/api_key.txt', 'r').read()
CITY = 'Guadalajara'

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius *  (9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']

temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']

wind_speed = response['wind']['speed']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time =dt.datetime.fromtimestamp(response['sys']['sunrise'], dt.timezone.utc)
sunset_time =dt.datetime.fromtimestamp(response['sys']['sunset'], dt.timezone.utc)


print(f'La temperatura en {CITY} es: {temp_celsius} °C, o tambien {temp_fahrenheit} °F')
print(f'La sensacion termica en {CITY} es: {feels_like_celsius} °C, o tambien {feels_like_fahrenheit} °F')
print(f'La humedad en {CITY} es: {humidity} %')
print(f'La velocidad del viento en {CITY} es: {wind_speed} m/s')
print(f'El sol sale a las {sunrise_time} y se mete a las {sunset_time}')
print(f'Una descripcion del clima en {CITY} es: {description}')

