# calculator.py

def add(a, b):
    # сложение
    pass

def subtract(a, b):
    # вычитание
    pass

def multiply(a, b):
    # умножение
    return a * b
    #pass

def divide(a, b):
    # деление
    pass

def main():
    # entering data and calling the required function
     # The main function
    expression = input("Enter an expression, for example 1+3 : ")  # Get string from user
    parts = expression.split()  #  Break the string by space-> ['1', '+', '3']
    a = float(parts[0])         # Convert first element to number
    operator = parts[1]         # The second element is the operator
    b = float(parts[2])         # Third element - second number

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
    pass
# This block ensures that the main function is called only 
# when the script is run directly.
if __name__ == "__main__":
    main()
