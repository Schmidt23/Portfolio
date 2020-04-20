import requests
import json
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OW_KEY')
KELVIN = 273.15

icons = {'01d':':sunny:', '02d':':partly_sunny:','03d':':white_sun_cloud:', '04d':':cloud:', '09d':':cloud_rain:',
         '10d': ':white_sun_rain_cloud:', '11d':':thunder_cloud_rain:', '13d': ':cloud_snow:', '50d':':fog:',
        '01n':':sunny:', '02n':':partly_sunny:','03n':':white_sun_cloud:', '04n':':cloud:', '09n':':cloud_rain:',
         '10n': ':white_sun_rain_cloud:', '11n':':thunder_cloud_rain:', '13n': ':cloud_snow:', '50n':':fog:',
         }

def give_weather(city):
    current = str(datetime.datetime.today().strftime("%Y-%m-%d-%H"))
    earlier = (datetime.datetime.today() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d-%H")
    filepath = f"weather/{city}-{current}.json"
    prev_filepath = f"weather/{city}-{earlier}.json"

    if not os.path.exists(filepath):
        print("made a fresh request")
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        with open(filepath, 'w') as f:
            json.dump(r.json(), f)

    try:
        os.remove(prev_filepath)
    except OSError:
        pass

    with open(filepath, 'r') as f:
        load = json.load(f)
    icon_id = load['weather'][0]['icon']
    icon = icons[icon_id]
    temp = load['main']['temp'] -KELVIN
    temp_min =load['main']['temp_min'] -KELVIN
    temp_max = load['main']['temp_max'] -KELVIN
    return icon, temp, temp_min, temp_max
