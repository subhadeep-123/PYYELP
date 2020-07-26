import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "terms": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [businesse["name"]
         for businesse in businesses if businesse["rating"] > 4.5]
print(names)

# To Iterate Over
for businesse in businesses:
    print(businesse["name"])
