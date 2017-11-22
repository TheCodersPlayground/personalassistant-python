from time import sleep

class masterHelper:
    def coolPrint(text):
        for a in text: 
            sleep(0.02)
            print(a, end='', flush=True)
        return ''
            