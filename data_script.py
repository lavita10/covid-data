#https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest

import os
import json 
import requests

base_url = "https://api.covid19api.com/"

if not os.path.exists('data'):
    os.mkdir('data')

def base():
    """
    Gets all the data from base url
    """
    data = {}
    req = requests.get(base_url)

    if req.status_code == 200:
        data = json.loads(req.text)
        #print(data.keys())
    return data

def get_day_one(country):
    """
    Gets all the data from base url
    """
    url = "{}dayone/country/{}/status/confirmed".format(base_url,country)
    data = {}
    req = requests.get(url)

    if req.status_code == 200:
        data = json.loads(req.text)
        #print(data.keys())


    return data

if __name__ == "__main__" :
    print(get_day_one("canada"))

