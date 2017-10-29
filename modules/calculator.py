def validateNumber():
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            continue

        if value < 0:
            print("Please enter a number greater than zero")
            continue
        else:
            break
    return value
    
def validateOperator():
    while True:
        if input(prompt) not in ('+', '-', '*', '/', '%', '^'):
            print ("Please enter a valid operator")
        else:
            break

def calculate(operator1,op,operation2):

    if op == '+':
        result = int(operator1) + int(operator2)
    elif op == '-':
        result = int(operator1) - int(operator2)
    elif op == '/':
        result = int(operator1) / int(operator2)
    elif op == '*':
        result = int(operator1) * int(operator2)
    elif op == '%':
        result = int(operator1) % int(operator2)
    elif op == '^':
        result = int(operator1) ^ int(operator2)
    
    return result

number1 = validateNumber("Please enter the first number: ")
operation1 = validateOperator("Please enter an operator you wish to use (+,-,*,/,%,^)")
number2 = validateNumber("Please enter the second number: ")

result = calculate(number1,operator1,number2)
print(result)