import requests
import datetime
import json
import os
import pandas as pd

today = str(datetime.datetime.today().strftime("%Y-%m-%d-%H"))
earlier = (datetime.datetime.today()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d-%H")


filepath = f"COVID19\{today}.json"
prev_filepath = f"COVID19\{earlier}.json"


def return_numbers():
    if not os.path.exists(filepath):
        print("made a fresh request")
        r = requests.get('https://covid2019-api.herokuapp.com/v2/total')
        with open(filepath, 'w') as f:
            json.dump(r.json(), f)

    try:
        os.remove(prev_filepath)
    except OSError:
        pass
    with open(filepath, 'r') as f:
        load = json.load(f)
        data = load['data']
        date_time = load['dt']
        confirmed = data["confirmed"]
        deaths = data["deaths"]
        recovered = data["recovered"]
        return confirmed, deaths, recovered, date_time


def current():


    if not os.path.exists(filepath):
        print('made a fresh request')
        alt = pd.read_html("https://www.worldometers.info/coronavirus/", header=0, index_col=0)[-1]
        df = pd.read_json(alt.to_json())
        with open(filepath, 'w') as f:
            json.dump(df.to_json(), f)
    try:
        os.remove(prev_filepath)
    except OSError:
        pass

    with open(filepath, 'r') as f:
        df = pd.read_json(json.load(f))
        confirmed = df['TotalCases'][-1]
        deaths = df['TotalDeaths'][-1]
        recovered = df['TotalRecovered'][-1]
        date_time = today
        return confirmed, deaths, recovered, date_time