import requests



def get_lati_longi(api_key, address):

   

    url = 'https://maps.googleapis.com/maps/api/geocode/json'

   

    params = {

        "address": address,

        "key": api_key

    }



    response = requests.get(url, params=params)



    if response.status_code == 200:

        data = response.json()

        if data["status"] == "OK":

            location = data["results"][0]["geometry"]["location"]

            lat = location["lat"]

            lng = location["lng"]

            return lat, lng

        else:

            print(f"Error: {data['error_message']}")

            return 0, 0

    else:

        print("Failed to make the request.")

        return 0, 0



api_key = "YOUR API KEY"

address = 'Vodickova 704/36, 11000 Prague 1, Czech Republic'



lati, longi = get_lati_longi(api_key, address)

print(f"Latitude: {lati}")

print(f"Longitude: {longi}")