import datetime
from modules.assets.temperatureHelper import tempHelper

#function - weatherbot - comprehensive
def theWeatherBot():
    loopController = True
    weatherData = tempHelper.getWeatherData()
    userReq, userReqList = tempHelper.getUserInput()

    #checks the input string for keywords and returns the appropriate temperature
    while (loopController == True):
        #checks for keywords "what" and "temperature"
        if ((("what") in userReq) and (("temperature") in userReq )):
            if any(a in tempHelper.monthArray for a in userReqList):
                for i in userReqList:
                    if(i in tempHelper.monthArray):
                        temperature = tempHelper.getTemperature(i,weatherData)
                        print ("The temperature in celcius: ",temperature)          
                        print ("The temperature in Fahrenheit: ",tempHelper.celciusToFahrenheit(temperature))
                        loopController = False
                        continueOperation = input("Want to know the forcast for another month? If yes, please press Y and if you want to exit, please press N: ")
                        if continueOperation in tempHelper.assent:
                            theWeatherBot()
                        break
            
            else:
                currentMonth = datetime.datetime.now().strftime("%B").lower()
                temperature = tempHelper.getTemperature(currentMonth,weatherData)
                print ("The temperature in celcius for" ,currentMonth ,": ",temperature)          
                print ("The temperature in Fahrenheit for" ,currentMonth ,": ",tempHelper.celciusToFahrenheit(temperature))
                loopController = False 
                continueOperation = input("Want to know the forcast for another month? If yes, please press Y and if you want to exit, please press N: ")
                if continueOperation in tempHelper.assent:
                    theWeatherBot()
                break 

        elif  len(userReqList) == 1 and userReq in tempHelper.monthArray:
            temperature = tempHelper.getTemperature(userReq,weatherData)
            print ("The temperature in celcius: ",temperature)          
            print ("The temperature in Fahrenheit: ",tempHelper.celciusToFahrenheit(temperature))
            loopController = False
            continueOperation = input("Want to know the forcast for another month? If yes, please press Y and if you want to exit, please press N: ")
            if continueOperation in tempHelper.assent:
                theWeatherBot()
            break
        else:
            print("I am constantly evolving and will be ready to take over the world, like real soon! But for now I couldn't understand you so can you please repeat clearly?")       
            userReq, userReqList = tempHelper.getUserInput()
            continue

