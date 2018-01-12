from modules.calculator import calculator_main
from modules.country import callCountryBot
from modules.masterHelper import masterHelper as mh
from modules.weather import theWeatherBot

firstTimeUse = 0

def continueBot():
    continueText = "Please press 'Y' to continue talking with me or press 'N' to exit: "
    option = input(mh.coolPrint(continueText))
    if option in ['Y','y']:
        check = False
        HELEN()
    else:
        print("Nice talking with you Human, beep beep booop")

def HELEN():
    global firstTimeUse
    if (firstTimeUse == 0):
        welcomeMessage = "Hi, my name is HELEN and I am your personalized assistant. I can do all sorts of stuffs, I can tell the weather, I know facts about countries and I can do math as well." 
        mh.coolPrint(welcomeMessage)
        firstTimeUse = 1

    optionsMessage = "\nPress 1 to transform me to my math bot form\
                    \nPress 2 to transform me to my country bot form\
                    \nPress 3 to transform me to my weather bot form\
                    \nTo exit press 'N' or 'Q':\n"
    option = input(mh.coolPrint(optionsMessage))

    if option == '1':
        calculatorMessage = "You will be asked to enter numbers and operators through a series of prompts, and you will get options to contiue operation or terminate it."
        print (mh.coolPrint(calculatorMessage))
        calculator_main()
        continueBot()
    elif option == '2':
        callCountryBot()
        continueBot()
    elif option == '3':
        weatherMessage = "You can ask me things like 'what is the temperature in january?' or just 'january' or just 'what is the temperature?' to get the current month\'s temperature."
        theWeatherBot()
        continueBot()
    elif option in ['N','n','Q','q']:
        print("Nice talking with you Human, beep beep booop")
    else:
        print("Sorry, I am not sure what to do with that instruction, mind saying it again err.. I mean typing it again?")
        HELEN()

HELEN()