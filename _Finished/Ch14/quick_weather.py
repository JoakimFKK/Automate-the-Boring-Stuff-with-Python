#! python3
import json
import os
import sys

import requests
# FIXME API Key

# Compute location from command line arguments
def daily_weather():
    if len(sys.argv) < 2:
        print("Usage: quick_weather.py location")
        sys.exit()
    location = ' '.join(sys.argv[1:])

    url = f'api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3'
    response = requests.get(url)
    response.raise_for_status()

    weather_data = json.loads(response.text)
    w = weather_data['list']
    print('Current weather in %s:' % (location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])



daily_weather()