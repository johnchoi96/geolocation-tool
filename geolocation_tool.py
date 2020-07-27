#!/usr/bin/python3

from Address import *
import requests


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

    results = jsonResponse["results"]
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
apiFile = open("apikey", "r")
apiKey = apiFile.read().strip()
apiFile.close()

url = generateUrl(address, apiKey)

latitude, longitude = jsonRequest(url)
print("Latitude:\t%.5f" % latitude)
print("Longitude:\t%.5f" % longitude)
