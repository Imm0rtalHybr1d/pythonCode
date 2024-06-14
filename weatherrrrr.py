import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    # Your API key (replace 'your_api_key' with an actual OpenWeatherMap API key)
    api_key = '5dd09ae78dfe16cade77b62b87b1b292'
    
    # Base URL for the OpenWeatherMap API
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Parameters for the API request
    params = {
        'q': city,       # City name
        'appid': api_key, # API key
        'units': 'metric' # Units of measurement (metric for Celsius)
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        # Extract and return relevant information
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        # Handle errors (e.g., city not found)
        return None

# Function to save weather data to a file
def save_weather_to_file(weather_data, filename):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write weather data to the file
        for key, value in weather_data.items():
            file.write(f"{key}: {value}\n")

# Main function
def main():
    # Ask the user for a city name
    city = input("Enter city name: ")
    
    # Get the weather data
    weather = get_weather(city)
    
    # Check if the weather data is available
    if weather:
        # Print the weather data
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")
        
        # Save the weather data to a file
        save_weather_to_file(weather, 'weather.txt')
        print("Weather data saved to 'weather.txt'.")
    else:
        print("City not found. Please try again.")

# Run the main function
if __name__ == '__main__':
    main()