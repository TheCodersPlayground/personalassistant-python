from time import sleep

class masterHelper:
    def coolPrint(text):
        for a in text:    
            print(a, end='', flush=True)
            sleep(0.025)