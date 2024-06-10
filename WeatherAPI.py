import requests
import sys
import json #allow python to interpret json files

API_key:str = '5dd09ae78dfe16cade77b62b87b1b292'
    
# City name (replace with your desired city)
city_name:str = "Cape Town"

standard_url:str = 'http://api.openweathermap.org/data/2.5/weather?'
complete_url =  f"{standard_url}q={city_name}&appid={API_key}" #forms the completed url using the diffrent variables such as city name and the API key
#you could also just manually type in the values like this :
#completed_url = 'http://api.openweathermap.org/data/2.5/weather?q=Cape Town&appid=5dd09ae78dfe16cade77b62b87b1b292'


request = requests.get(complete_url)
weather_data = request.json()

def convert_to_celcius(temp:float) -> float:
    celsius = (temp-273.15)  # Conversion formula
    return celsius

city_name:str = weather_data['name'] #gets name of the city

forcast:str = weather_data["weather"][0]["description"] #gets weather discription 

temperature:float = weather_data['main']['temp'] #gets current temp

max_temp: float = weather_data['main']['temp_max'] #gets max temp for the day
min_temp: float = weather_data['main']['temp_min'] #gets min temp for the day

#converts temp to celcius and stores them in new variables
new_max_temp = convert_to_celcius(max_temp)
new_min_temp = convert_to_celcius(min_temp)
new_normal_temp = convert_to_celcius(temperature)
    
print(f'The weather for {city_name} today is {forcast}') 
print(f'Temps: high/low >>> {new_max_temp:,.0f}°C/ {new_min_temp:,.0f}°C Feels like {new_normal_temp:,.0f}°C')
print()

  


   