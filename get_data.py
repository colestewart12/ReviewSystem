import csv
import requests
from get_tempfar import getTempFar

# API KEY GOES AFTER BEARER IN AUTHORIZATION IN HEADERS FOR REQUESTS

locations = ["Tacoma", "Seattle", "Portland", "San Francisco", "Los Angeles"]
location_long_lat_mapping = {
    "Tacoma": (47.3, 122.4),
    "Seattle": (47.6, 122.3),
    "Portland": (45.5, 122.7),
    "San Franciso": (37.8, 122.4),
    "Los Angeles": (34.1, 118.2)
}
business_info = []

# getting business ids for 20 restaurants in each location
for location in locations:
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term=Food&sort_by=best_match&limit=5"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer"
    }

    response = requests.get(url, headers=headers)
    businesses = response.json()

    for business in businesses['businesses']:
        business_info.append((business['id'], location))

def add_data_to_csv(new_reviews, csv_fil, location):
    fieldnames = ['text', 'rating', 'weather', 'time_created', 'location']

    with open(csv_fil, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # If the file is empty, write headers
        if file.tell() == 0:
            writer.writeheader()

        # Check if 'reviews' key exists in the response
        if 'reviews' in new_reviews:
            for review in new_reviews['reviews']:
                review_time_created = review['time_created']
                longitude = location_long_lat_mapping[location][0]
                lattitude = location_long_lat_mapping[location][1]
                weatherFarenheit = getTempFar(longitude, lattitude, review_time_created)

                writer.writerow({
                    'text': review['text'],
                    'rating': review['rating'],
                    'weather': weatherFarenheit,
                    'time_created': review_time_created,
                    'location': location
                })
        else:
            print(f"No reviews found for location: {location}")

for business in business_info:
    url = "https://api.yelp.com/v3/businesses/" + business[0] + "/reviews?limit=50&sort_by=yelp_sort&page=25"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer"
    }
    response = requests.get(url, headers=headers)
    reviews = response.json()

    csv_file = 'reviews.csv'
    add_data_to_csv(reviews, csv_file, business[1])
