import requests
import json
import configparser
import os

config_file = 'config.ini'

# Check if the config.ini file exists
if not os.path.exists(config_file):
    raise FileNotFoundError(f"{config_file} not found. Please create a configuration file with the API key.")

# Read the API key from the config.ini file
config = configparser.ConfigParser()
config.read(config_file)
api_key = config.get('api', 'key')

# Replace 'city_name' with the name of the city for which you want the weather data
lat = '47.25'
lon = '15.21'

# Base URL for the weather API
# api.openweathermap.org/data/2.5/weather?q=London&appid={API key}
# base_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

# Building the complete URL with the city name and API key
complete_url = f'{base_url}lat={lat}&lon={lon}&appid={api_key}'
# complete_url = f'{base_url}q=London&appid={api_key}'

# Making a GET request to the API
response = requests.get(complete_url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()

    # Save the JSON data to a file
    with open('weather_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print('The weather API data has been saved as weather_data.json.')
else:
    print(f'Error: Unable to fetch weather data. Status code: {response.status_code}')
