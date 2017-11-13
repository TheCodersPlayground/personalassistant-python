from modules.calculator import calculator_main
from modules.country import callCountryBot
from modules.masterHelper import masterHelper as mh
from modules.weather import theWeatherBot

welcomeMessage = "Hi, my name is HELEN and I am your personalized assistant. I can do all sorts of stuffs, I can tell the weather, I know facts about countries and I can do math as well."
optionsMessage = "\nPress 1 to transform me to my math bot form\
                 \nPress 2 to transform me to my country bot form\
                 \nPress 3 to transform me to my weather bot form: \n"
mh.coolPrint(welcomeMessage)

option = input(mh.coolPrint(optionsMessage))

if option == '1':
    calculator_main()
elif option == '2':
    callCountryBot()
elif option == '3':
    theWeatherBot()
    
    