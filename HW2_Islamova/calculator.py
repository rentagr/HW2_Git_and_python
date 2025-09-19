# calculator.py

AVAILABLE_OPERATORS = ['+', '-', '*', '/']

def add(a, b):
    result = a+b
    return result

def subtract(a, b):
    result = a - b
    return result

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
    # expression = input("Enter an expression, for example 1+3 : ")  # Get string from user
    # TODO: есть ошибки в цикле, нужно исправить
    condition = True
    while condition: 
        a = input("Input first number: ")
        operator = str(input("Enter math operation: "))
        b = input("Input second operator: ")

        # TODO: нужен более корректный метод проверки на число: целое, с плавающей точкой, и отрицательное
        if a.isnumeric() and b.isnumeric() and operator in AVAILABLE_OPERATORS:
            a, b = float(a), float(b)
            condition = False
        else:
            print("Input natural number")
   
    # TODO: на удаление, если подать 1234+7484, то будет ошибка
    #parts = expression.split()  #  Break the string by space-> ['1', '+', '3']
    #a = float(parts[0])         # Convert first element to number
    #operator = parts[1]         # The second element is the operator
    #b = float(parts[2])         # Third element - second number

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
def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not possible")
        return None
    
    return a / b