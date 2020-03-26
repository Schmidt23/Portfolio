import requests
import json

def get_def(word):
    r = requests.get(f'https://api.urbandictionary.com/v0/define?term={word}')
    defs = r.json()['list'][0]['definition']
    return defs

#print (get_def("simp"))