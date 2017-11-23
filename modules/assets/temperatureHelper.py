import json
import random

class tempHelper:
    def celciusToFahrenheit(celcius):
        fahrenheit = (9/5) * celcius + 32
        return float("{0:.1f}".format(fahrenheit))
    
    #gets the average, max and min temperature for each month from a json file and parses it
    def getWeatherData():
        with open("modules/assets/weatherInfo.json") as weatherRawData:
            weatherData = json.load(weatherRawData)
        return weatherData
    
    #returns a random temperature based on the weather data for the month
    def getTemperature(i,weatherData):
        temperature = random.uniform(float(weatherData[i]["Coldest"]),float(weatherData[i]["Warmest"]))
        temperatureFormated = float("{0:.1f}".format(temperature))
        return temperatureFormated

    #gets the input
    def getUserInput():
        userReq = input("Please ask me for which month you want to know the temperature: ")
        userReqFormated = userReq.lower()
        userReqList = userReqFormated.split(' ')
        return userReqFormated, userReqList

    monthArray = ["january", "february","march","april","may","june","july","august","september","october","november","december"]
    assent = ["yes","YES","Y","Yes","y"]