import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        
        weather_info = {
            "City": data['name'],
            "Temperature": main['temp'],
            "Pressure": main['pressure'],
            "Humidity": main['humidity'],
            "Weather": weather['description'],
            "Wind Speed": wind['speed']
        }
        return weather_info
    else:
        return None

def display_weather(weather_info):
    if weather_info:
        print(f"City: {weather_info['City']}")
        print(f"Temperature: {weather_info['Temperature']} °C")
        print(f"Pressure: {weather_info['Pressure']} hPa")
        print(f"Humidity: {weather_info['Humidity']}%")
        print(f"Weather: {weather_info['Weather']}")
        print(f"Wind Speed: {weather_info['Wind Speed']} m/s")
    else:
        print("City not found or API request failed.")

if __name__ == '__main__':
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name, api_key)
    display_weather(weather_info)
