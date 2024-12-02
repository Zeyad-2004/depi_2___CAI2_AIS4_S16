import time
from calc import add, sub, mult, div


############################# FUNCTIONS #############################
def error_message(error_type):
    print()
    if(error_type == 0): # Invalid Operation
        print("! Invalid Operation !")
        time.sleep(1)
        print("Please enter a value from the list")
    elif(error_type == 1): # Not numerical input
        print("PLEASE enter a numrical value ONLY !")
    elif(error_type == 2): # ZeroDivisionError
        print("!! Zero-Division Error !!")
        time.sleep(1)
        print("Make sure the demonator not be ZERO")
    # elif(error_type == 3): # Value Error
    print()
    time.sleep(4)

def numerical_input_handler(message=": "):
    try:
        number = 0
        number = int(input(message))
        
        return number

    except ValueError:
        error_message(1)
        raise ValueError


def get_calcutation_operation():
    print()
    time.sleep(0.8)
    print("Choose the operation:")
    time.sleep(0.2)
    print("1: add (+)")
    time.sleep(0.2)
    print("2: sub (-)")
    time.sleep(0.2)
    print("3: multiply (*)")
    time.sleep(0.2)
    print("4: division (/)")
    time.sleep(0.2)
    print("0: EXIT")
    time.sleep(0.5)

    try:
        operation = numerical_input_handler(": ")

        if operation < 0 or operation > 4:
            error_message(0)
        else:
            return operation

    except ValueError:
        error_message(1)
    
    return -1

def do_calculation(num1, num2, operation):
    sign = ''
    result = 0

    if(operation == 1):
        sign = '+'
        result = add(num1, num2)
    elif(operation == 2):
        sign = '-'
        result = sub(num1, num2)
    elif(operation == 3):
        sign = '*'
        result = mult(num1, num2)
    elif(operation == 4):
        sign = '/'
        try:
            result = div(num1, num2)
        except ZeroDivisionError:
            raise ZeroDivisionError
    
    print()
    print(f"The result for: {num1} {sign} {num2} = {result}\n\n", end="")
    time.sleep(2)

def calculator():
    while(True):
        try:
            print()
            num1 = numerical_input_handler("Enter the first number: ")
            num2 = numerical_input_handler("Enter the second number: ")
        except ValueError:
            print("Try again!")

            if(input("-Press [ Enter ] to continue Else enter any character to exit: ") != ""):
                return 1
            else:
                continue

        while(True):
            operation = get_calcutation_operation()

            if(operation == -1):
                print("Try Again!")
            elif(operation == 0):
                return 1
            else:
                try:
                    do_calculation(num1, num2, operation)
                    break
                except ZeroDivisionError:
                    error_message(2)
                    print("Try Again!\n")
                    

        print("Do you like to do another operatoin?")
        
        if(input("-Press [ Enter ] to continue Else enter any character to exit: ") != ""):
            return 1
        else:
            return 0


######################### Program Start #########################

print("Welcome to the Calculator module you can do (+, -, *, /) calculations on two numbers.")
time.sleep(1)
print(". ", end="")
time.sleep(0.7)
print(". ", end="")
time.sleep(0.7)
print(". ")
time.sleep(0.7)

while(True):
    if(calculator()):
        break
    

time.sleep(0.5)
print("\nThanks for using the Calculator module.")
