#!/usr/bin/python3

from geopy.geocoders import Nominatim
import sys


# =====================
# FUNCTIONS
# =====================
def getAddress() -> str:
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("Zip: ")
    return "%s, %s, %s %s" % (street, city, state, zipcode)


def getManualAddress() -> str:
    addr = input("Enter full address> ")
    while len(addr) == 0 and addr == "":
        addr = input("Enter full address> ")

    return addr


# =====================
# MAIN
# =====================
locator = Nominatim(user_agent="geolocation-tool")

# get address from user
selection = input("Press 1 for US address or 2 for manual address entry> ")
while selection != "1" and selection != "2":
    selection = input("Press 1 for US address or 2 for manual address entry> ")

if selection == "1":
    address = getAddress()
else:
    address = getManualAddress()

try:
    location = locator.geocode(address)

    lat = location.latitude
    lon = location.longitude

    print("Latitude:\t%.5f" % lat)
    print("Longitude:\t%.5f" % lon)
except Exception:
    print("Invalid address")
    sys.exit(-1)
