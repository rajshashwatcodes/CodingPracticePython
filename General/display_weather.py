import requests
import json

API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {city}")
        return None

def display_weather(data):
    city = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_data = get_weather(city)
        if weather_data:
            display_weather(weather_data)

if __name__ == "__main__":
    main()
