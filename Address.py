#!/usr/bin/python3


class Address:

    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def getStreet(self) -> str:
        delimitedStreet = self.street.split(" ")
        street = delimitedStreet[0]
        for i in range(1, len(delimitedStreet)):
            street += "+" + delimitedStreet[i]

        return street

    def getState(self) -> str:
        delimitedState = self.state.split(" ")
        state = delimitedState[0]
        for i in range(1, len(delimitedState)):
            state += "+" + delimitedState[i]

        return state
