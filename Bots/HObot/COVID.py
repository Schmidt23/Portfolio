import requests
import datetime
import json
import os

today = str(datetime.datetime.today().strftime("%Y-%m-%d-%H"))
earlier = (datetime.datetime.today()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d-%H")


filepath = f"COVID19\{today}.json"
prev_filepath = f"COVID19\{earlier}.json"

if not os.path.exists(filepath):
    print("made a fresh request")
    r = requests.get('https://covidapi.info/api/v1/global')
    with open(filepath, 'w') as f:
        json.dump(r.json(), f)

try:
    os.remove(prev_filepath)
except OSError:
    pass


def return_numbers():
    with open(filepath, 'r') as f:
        data = json.load(f)["result"]
        confirmed = data["confirmed"]
        deaths = data["deaths"]
        recovered = data["recovered"]
        return confirmed, deaths, recovered
