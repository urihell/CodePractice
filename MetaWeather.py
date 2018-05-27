import requests



def location_id(location):
    """DOCSTRING: Get location input and return the location ID, also called 'woeid' """

    r = requests.get(f'https://www.metaweather.com/api/location/search/?query={location}')
    woeid = (r.json()[0]['woeid'])
    return woeid


def weather(woeid):
    """DOCSTRING Get weather for next 6 days. Day 7 needs to be added"""

    r = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
    data = (r.json()['consolidated_weather'])
    for n in data:
        print(f'\n\nDate: {n["applicable_date"]}')
        print(f'Min Temp: {round(n["min_temp"], 2)}')
        print(f'Max Temp: {round(n["max_temp"], 2)}')
        print(f'Forecast: {n["weather_state_name"]}')


search_loc = location_id(input('Enter location:\n'))
weather(search_loc)
