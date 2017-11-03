import json

class countryHelper:
    def getInput():
        keyString = input("Please enter what you need to know in the following format {Field} of {Country} or enter just the {field} to get the summarized country details: ")
        inputList = keyString.split(" of ")
        return keyString, inputList

    def getCountryData():
        with open('assets/country.json') as json_data:
            countryData = json.load(json_data)
        return countryData
