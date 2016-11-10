import urllib.request   # urlencode function
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
MBTA_URL = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw'


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    new_name = place_name.replace(" ", "%20")  #convert space to %20;
    url = GMAPS_BASE_URL + '?address=' + new_name
    place_json = get_json(url)
    lat = place_json['results'][0]['geometry']['location']['lat']
    lon = place_json['results'][0]['geometry']['location']['lng']
    return [lat, lon]


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    lat = '%f' % latitude
    lon = '%f' % longitude
    url = MBTA_URL + '&lat=' + lat + '&lon=' + lon 
    station_json = get_json(url)
    nearest_station = station_json['stop'][0]['stop_name']
    distance = station_json['stop'][0]['distance']
    return [nearest_station, distance]


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat = get_lat_long(place_name)[0]
    lon = get_lat_long(place_name)[1]
    get_nearest_station(lat, lon)
    a = get_nearest_station(lat, lon)[0]  #nearest station
    b = get_nearest_station(lat, lon)[1]  #distance
    return (a, b)

def main():
    place = input("Please enter the name of the place!")
    print("The nearest Station from ", place, " is:")
    print(find_stop_near(place))
    
    
if __name__ == '__main__':
    main()                  # only works with addresses in Boston. Others shows up as out of index