def validateNumber(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            continue

        if value < 0:
            print("Please enter a number greater than zero")
            continue
        else:
            break
    return value
    
def validateOperator(prompt):
    while True:
        value = input(prompt)
        if value not in ('+', '-', '*', '/', '%', '^'):
            print ("Please enter a valid operator")
        else:
            break
    return value
        

def calculate(operator1,op,operator2):
    result = 0
    if op == '+':
        result =  (operator1) +  (operator2)
    elif op == '-':
        result =  (operator1) -  (operator2)
    elif op == '/':
        result =  (operator1) /  (operator2)
    elif op == '*':
        result =  (operator1) *  (operator2)
    elif op == '%':
        result =  (operator1) %  (operator2)
    elif op == '^':
        result =  (operator1) **  (operator2)
    
    return result

number1 = validateNumber("Please enter the first number: ")
operation1 = validateOperator("Please enter an operator you wish to use (+,-,*,/,%,^)")

number2 = validateNumber("Please enter the second number: ")

result = calculate(number1,operation1,number2)

print ("The result of ",number1,operation1,number2,"is", result)


