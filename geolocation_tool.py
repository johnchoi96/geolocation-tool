#!/usr/bin/python3

from Address import *
import requests
import sys


# =====================
# FUNCTIONS
# =====================
def getAddress() -> Address:
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zip: ")
    return Address(street, city, state, zipcode)


def generateUrl(addr: Address, apikey: str) -> str:
    return "https://api.geocod.io/v1.6/geocode?street=%s&city=%s&state=%s&api_key=%s" \
           % (addr.getStreet(), addr.city, addr.getState(), apikey)


def jsonRequest(jsonUrl):
    response = requests.get(jsonUrl)
    jsonResponse = response.json()

    try:
        results = jsonResponse["results"]
    except KeyError:
        raise ValueError("Invalid address")
    lat = results[0]["location"]["lat"]
    long = results[0]["location"]["lng"]
    accuracy = results[0]["accuracy"]
    for result in results:
        if result["accuracy"] > accuracy:
            lat = result["location"]["lat"]
            long = result["location"]["lng"]
    return lat, long


# =====================
# MAIN
# =====================

# get address from user
address = getAddress()

# read the api key from the file
try:
    apiFile = open("apikey", "r")
except FileNotFoundError:
    print("File containing api key cannot be opened.\nObtain an api key from https://www.geocod.io and save api key"
          " to a file named apikey (no extensions)")
    sys.exit(-1)

apiKey = apiFile.read().strip()
apiFile.close()

url = generateUrl(address, apiKey)

try:
    latitude, longitude = jsonRequest(url)
except ValueError as e:
    print(e)
    sys.exit(-1)
print("Latitude:\t%.5f" % latitude)
print("Longitude:\t%.5f" % longitude)
