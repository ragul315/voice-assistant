import requests
from t2s import speek
api_key = '001f26759dc53ba48cd55e7b5d4160a5'

def get_weather(location=None):
    print("Location:", location)  # Add this line to print out the captured location
    # Rest of the function...

    if not location:
        # Get latitude and longitude of the current location
        location_response = requests.get("http://ip-api.com/json/")
        location_data = location_response.json()
        
        # Extract latitude and longitude from location data
        lat = location_data.get('lat')
        lon = location_data.get('lon')
        print(lat,"\n",lon)
        
        if not lat or not lon:
            return "Failed to fetch location data."
        
        # API endpoint to fetch weather data based on latitude and longitude
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    else:
        # API endpoint to fetch weather data based on city name
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Fetch weather data
    response = requests.get(url)
    
    # Check if the response status code is not 200 (OK)
    if response.status_code != 200:
        return "Failed to fetch weather data."
    
    weather_data = response.json()
    
    # Check if 'main' key exists in weather_data
    if 'main' not in weather_data or 'weather' not in weather_data:
        return "Failed to fetch weather data."
    
    # Extract required information from weather data
    temperature = weather_data['main'].get('temp')
    description = weather_data['weather'][0].get('description')
    city = weather_data.get('name')
    
    # Create a sentence with the weather information
    weather_sentence = f"The current weather in {city} is {description} with a temperature of {temperature}°C."
    
    return weather_sentence

