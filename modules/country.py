import json
from modules.assets.countryHelper import countryHelper

def getData():
    countryData = countryHelper.getCountryData()
    keyString, inputList = countryHelper.getInput()
    return inputList, countryData

def countryBot(inputList, countryData):
    if (len(inputList)==2):
        try:
            information = countryData[inputList[1]][inputList[0]]
            print (information)
            decision = input("You want to continue learn about the numbers related to countries? Press Y or N:")
            if decision == "y" or decision == "Y":
                keyString, inputList = countryHelper.getInput()
                countryBot(inputList, countryData)
        except:
            print ("I don't think I know what you asked, please ask me something I know!")
            keyString, inputList = countryHelper.getInput()
            countryBot(inputList, countryData)

    elif (len(inputList) == 1 ):
        count = 0
        try:
            for a in countryData:
                if count <= 10:
                    print(countryData[a][inputList[0]])
                    count = count + 1
            decision = input("You want to continue learn about the numbers related to countries? Press Y or N:")
            if decision == "y" or decision == "Y":
                keyString, inputList = countryHelper.getInput()
                countryBot(inputList, countryData)
        except KeyError:
            print ("I don't think I know what you asked, please ask me something I know!")
            keyString, inputList = countryHelper.getInput()
            countryBot(inputList, countryData)
def callCountryBot():
    inputList, countryData = getData()
    countryBot(inputList, countryData)