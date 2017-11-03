import json
from assets.countryHelper import countryHelper

countryData = countryHelper.getCountryData()
keyString, inputList = countryHelper.getInput()

def countryBot(inputList):
    if (len(inputList)==2):
        try:
            information = countryData[inputList[1]][inputList[0]]
            print (information)
            decision = input("You want to continue learn about the numbers related to countries? Press Y or N:")
            if decision == "y" or decision == "Y":
                keyString, inputList = countryHelper.getInput()
                countryBot(inputList)
        except:
            print ("I don't think I know what you asked, please ask me something I know!")
            keyString, inputList = countryHelper.getInput()
            countryBot(inputList)

    elif (len(inputList) == 1 ):
        count = 0
        try:
            for a in countryData:
                if count <= 10:
                    print(countryData[a][inputList[0]])
                    count = count + 1
        except KeyError:
            print ("I don't think I know what you asked, please ask me something I know!")
            keyString, inputList = countryHelper.getInput()
            countryBot(inputList)

countryBot(inputList)