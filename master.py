from modules.calculator import calculator_main
from modules.country import callCountryBot
from time import sleep

welcomeMessage = "Hi, my name is HELEN and I am your personalized assistant. I can do all sorts of stuffs, I can tell the weather, I know facts about countries and I can do math as well."

def coolPrint(text):
    for a in text:    
        print(a, end='', flush=True)
        sleep(0.025)

coolPrint(welcomeMessage)