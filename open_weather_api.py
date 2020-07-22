# This file is meant to contain all examples of successful calls to open weather api,
# following https://rapidapi.com/community/api/open-weather-map?endpoint=53aa6041e4b00287471a2b62

import requests

city_list = ['london', 'berlin', 'brussels', 'vilnius']


class City:
    def __init__(self, city_name):
        self.city_name = city_name

    def request_weather(self):
        """Current Weather Data

        Args:
            city (string): name of the input city

        Returns:
            response: response as json object
        """
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        #querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"london"}
        querystring = {"callback": "test", "units": "metric",
                    "mode": "xml%2C html", "q": self.city_name}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        return response.text

    def search_weather(self):
        """Search weather data

        Args:
            city_list (string): name of the input city

        Returns:
            response: response as json object
        """

        url = "https://community-open-weather-map.p.rapidapi.com/find"

        querystring = {"type": "link%2C accurate",
                    "units": "metric", "q": self.city_name}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        return response.text  

    def historical_weather(self): #PROBLEM WITH LOCATION: only lon lat available
        """Search historical weather data

        Args:
            city_list (string): name of the input city

        Returns:
            response: response as json object
        """
        # Historical Weather Data
        import requests

        url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

        querystring = {"lat":"37.774929","lon":"-122.419418","dt":"1595243722","units": "metric"}        

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.text


    def five_days_forecast_weather(self):
        """5 day / 3 hour forecast weather data

        Args:
            city_list (string): name of the input city

        Returns:
            response: response as json object
        """

        url = "https://community-open-weather-map.p.rapidapi.com/forecast"

        querystring = {"units": "metric", "q": self.city_name}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "84a315f297msh04bc1c02d9bf9afp123b82jsn2ba923f95520"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)



city1 = City('vilnius')
#city2 = City('namur')

#print(city1.request_weather())
#print(city2.request_weather())

#print(city1.search_weather())
#print(city2.search_weather())

print(city1.historical_weather())
#print(city1.five_days_forecast_weather())






#response = request_weather(city_list[-1])
#response = search_weather(city_list[-1])
#print(city_list[0], response.text)