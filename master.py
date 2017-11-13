from modules.calculator import calculator_main
from modules.country import callCountryBot
from modules.masterHelper import masterHelper as mh
from modules.weather import theWeatherBot

def continueBot():
    continueText = "Please press 'Y' to continue talking with me or press 'N' to exit: "
    option = input(mh.coolPrint(continueText))
    if option in ['Y','y']:
        check = False
        HELEN()
    else:
        print("Nice talking with you Human, beep beep booop")

def HELEN():
    welcomeMessage = "Hi, my name is HELEN and I am your personalized assistant. I can do all sorts of stuffs, I can tell the weather, I know facts about countries and I can do math as well."
    optionsMessage = "\nPress 1 to transform me to my math bot form\
                    \nPress 2 to transform me to my country bot form\
                    \nPress 3 to transform me to my weather bot form\
                    \nTo exit press 'N' or 'Q':\n"
    mh.coolPrint(welcomeMessage)

    option = input(mh.coolPrint(optionsMessage))

    if option == '1':
        calculator_main()
        continueBot()
    elif option == '2':
        callCountryBot()
        continueBot()
    elif option == '3':
        theWeatherBot()
        continueBot()
    elif option in ['N','n','Q','q']:
        print("Nice talking with you Human, beep beep booop")
    else:
        print("Sorry, I am not sure what to do witht that instruction, mind saying it again err.. I mean typing it again?")
        HELEN()

HELEN()