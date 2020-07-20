# This file is meant to contain all examples of successful calls to open weather api, 
# following https://rapidapi.com/community/api/open-weather-map?endpoint=53aa6041e4b00287471a2b62 

import requests

city_list = ['london','berlin','brussels','vilnius']


def request_weather(city):
    """Current Weather Data

    Args:
        city (string): name of the input city

    Returns:
        response: response as json object
    """
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    #querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"london"}
    querystring = {"callback":"test","units":"metric","mode":"xml%2C html","q":city}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

response = request_weather(city_list[0])
print(city_list[0], response.text)


'''
# Search weather data WORKS
import requests

url = "https://community-open-weather-map.p.rapidapi.com/find"

querystring = {"type":"link%2C accurate","units":"imperial%2C metric","q":"florence"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
'''

'''
# Historical Weather Data
import requests

url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

querystring = {"lat":"37.774929","lon":"-122.419418","dt":"1595243722"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
'''

'''
# 5 day / 3 hour forecast data

import requests

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring = {"q":"london"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
'''