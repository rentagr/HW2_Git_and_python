# calculator.py

AVAILABLE_OPERATORS = ['+', '-', '*', '/']

def add(a, b):
    result = a+b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not possible")
        return None
    return a / b

def is_number(s):
    """Checks whether the string is a number (integer, fractional, negative)"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    # entering data and calling the required function
    # The main function
    # expression = input("Enter an expression, for example 1+3 : ")  # Get string from user
    condition = True
    while condition: 
        a = input("Input first number: ")
        operator = input("Enter math operation: ")
        b = input("Input second number: ")

        if is_number(a) and is_number(b) and operator in AVAILABLE_OPERATORS:
            a, b = float(a), float(b)
            condition = False
        else:
            print("Please, input valid numbers and operator (+,-,*,/)")
   

    # Depending on the operator, we call the appropriate function
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Unknown operator!")
        return

    print(result) # Print result
    
# This block ensures that the main function is called only 
# when the script is run directly.
if __name__ == "__main__":
    main()
