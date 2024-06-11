import requests

class Weather:
    API_key:str = '5dd09ae78dfe16cade77b62b87b1b292'
    standard_url:str = 'http://api.openweathermap.org/data/2.5/weather?'
    
    def __init__(self,city_name:str) -> None:
        self.city_name = city_name
    
    @staticmethod
    def convert_to_celcius(temp:float) -> float:
        celsius = (temp-273.15)  # Conversion formula
        return celsius

    
        
    def get_weather(self) -> None:
        complete_url =  f"{self.standard_url}q={self.city_name}&appid={self.API_key}"
        
        request = requests.get(complete_url)
        weather_data = request.json()
        forcast:str = weather_data["weather"][0]["description"] #gets weather discription 

        temperature:float = weather_data['main']['temp'] #gets current temp

        max_temp: float = weather_data['main']['temp_max'] #gets max temp for the day
        min_temp: float = weather_data['main']['temp_min'] #gets min temp for the day

        #converts temp to celcius and stores them in new variables
        new_max_temp = self.convert_to_celcius(max_temp)
        new_min_temp = self.convert_to_celcius(min_temp)
        new_normal_temp = self.convert_to_celcius(temperature)
        
        print(f'The weather for {self.city_name} today is {forcast}') 
        print(f'Temps: high/low >>> {new_max_temp:,.0f}°C/ {new_min_temp:,.0f}°C Feels like {new_normal_temp:,.0f}°C')
        print()

