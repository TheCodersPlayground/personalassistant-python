#function to validate a number, accepts one variable
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

#function to validate operator
def validateOperator(prompt):
    while True:
        value = input(prompt)
        if value not in ('+', '-', '*', '/', '%', '^'):
            print ("Please enter a valid operator")
        else:
            break
    return value

#determines if the result is to be preserved or cleared for next operation
def askDecision():
    decision = validateDecision("Do you want to continue the operation?\n Press 1 to continue operation,\
\n Press 2 to clear the result and start a new calculation \n Press 3 to Exit calculator\n")
    return decision


def validateDecision(prompt):
    while True:
        value = input(prompt)
        if value not in ('1','2','3'):
            print ("Please enter a valid decision")
        else:
            break
    return value

def calculate(operator1,op,operator2):
    result = 0
    if op == '+':
        result =  (operator1) +  (operator2)
        printResult(operator1,op,operator2,result)
    elif op == '-':
        result =  (operator1) -  (operator2)
        printResult(operator1,op,operator2,result)
    elif op == '/':
        #Logic to avoid DivideByZero exception
        try:
            result =  (operator1) /  (operator2)
            printResult(operator1,op,operator2,result)
        except ZeroDivisionError:
            print("The second operator cannot be zero")
            result = repeatSecondInput(operator1,op,operator2)
    elif op == '*':
        result =  (operator1) *  (operator2)
        printResult(operator1,op,operator2,result)
    elif op == '%':
        result =  (operator1) %  (operator2)
        printResult(operator1,op,operator2,result)
    elif op == '^':
        result =  (operator1) **  (operator2)
        printResult(operator1,op,operator2,result)  
    return result

#function to continue calculation with the existing result or start a new calculation
def continueCalculation(result):
    while True:
        decision = askDecision()
    
        if decision == '1':
            operation2 = validateOperator("Please enter an operator you wish to use on the previous result (+,-,*,/,%,^): ")
            number3 = validateNumber("Please enter the next number: ")
            result1 = calculate(result, operation2, number3)
            print ("The result  ",result, operation2, number3,"is", result1)
            result = result1
            continue
        elif decision == '2':
            number1 = validateNumber("Please enter the first number: ")
            operation1 = validateOperator("Please enter an operator you wish to use (+,-,*,/,%,^): ")
            number2 = validateNumber("Please enter the second number: ")
            result = calculate(number1,operation1,number2)
            print ("The result  ",number1, operation1, number2,"is", result)
            continue
        elif decision == '3':
            break
    
#function helper to prevent DivideByZero exception
def repeatSecondInput(number1,operation1,number2):
    number2 = validateNumber("Please enter the second number: ")
    result = calculate(number1,operation1,number2)
    return result

def printResult(number1,operation1,number2,result):
     print ("The result of ",number1, operation1, number2,"is", result)

#entry point function of the calculator program
def calculator_main():
    number1 = validateNumber("Please enter the first number: ")
    operation1 = validateOperator("Please enter an operator you wish to use (+,-,*,/,%,^): ")
    number2 = validateNumber("Please enter the second number: ")
    result = calculate(number1,operation1,number2)
    continueCalculation(result)