import requests
from datetime import datetime

locations = ["Tacoma", "Seattle", "Portland", "San Francisco", "Los Angeles"]

# for location in locations:
#     url = (f"https://api.tomorrow.io/v4/weather/history/recent?location={location}&timesteps=1d&apikey"
#            "=Dd7tXo9BK5CTPQeUcr2QeKtbLakzVgzn")
#
#     headers = {"accept": "application/json"}
#
#     response = requests.get(url, headers=headers)
#
#     data = response.json()
#
#     print(data['timelines']['daily'][1]['values']['temperatureAvg'])

# url = "https://api.tomorrow.io/v4/weather/history/recent?location=austin&timesteps=1h&apikey=kK87NiK2JaI7ktE2pnZZ73TsGsz59BI7"
# date = "2024-03-23 19:49:33"
# hour = date.split(" ")[1].split(":")[0]
# headers = {"accept": "application/json"}
#
# response = requests.get(url, headers=headers)
# data = response.json()
# print(data['timelines']['hourly'])
#
# timetemp = data['timelines']['hourly']
#
# matching_objects = [obj for obj in timetemp if datetime.strptime(obj['time'], '%Y-%m-%dT%H:%M:%SZ').hour == int(hour)]
# temperature = matching_objects[0]['values']['temperature'] * 9/5 + 32


def getTempFar(lat, lon, date):
    url = f"https://api.tomorrow.io/v4/weather/history/recent?location={lat},{lon}&timesteps=1h&apikey=kK87NiK2JaI7ktE2pnZZ73TsGsz59BI7"
    hour = date.split(" ")[1].split(":")[0]
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data['timelines']['hourly'])

    timetemp = data['timelines']['hourly']

    matching_objects = [obj for obj in timetemp if
                        datetime.strptime(obj['time'], '%Y-%m-%dT%H:%M:%SZ').hour == int(hour)]
    temperature = matching_objects[0]['values']['temperature'] * 9 / 5 + 32
    return temperature


date = "2024-03-23 19:49:33"
lat = 39.9
lon = -88.8

print(getTempFar(lat, lon, date))