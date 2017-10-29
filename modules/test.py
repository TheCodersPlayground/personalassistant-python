def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("Please enter a valid number.")
            continue
        else:
            break
    return value

def get_operator(prompt):
    while True:
        if input(prompt) not in ('+', '-', '*', '/', '%', '^'):
            print ("Please enter a valid operator")
        else:
            break


def calculate():
    
    if operator1 == '+':
        result = int(number1) + int(number2)
    elif operator1 == '-':
        result = int(number1) - int(number2)
    elif operator1 == '/':
        result = int(number1) / int(number2)
    elif operator1 == '*':
        result = int(number1) * int(number2)
    elif operator1 == '%':
        result = int(number1) % int(number2)
    elif operator1 == '^':
        result = int(number1) ^ int(number2)
    
    return result

number1 = get_int("Please enter the first number: ")
operator1 = get_operator("Please enter an operator you wish to use (+,-,*,/,%,^)")
number2 = get_int("Please enter the second number: ")

result = calculate()
print(result)



