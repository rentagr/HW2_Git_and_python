# calculator.py

AVAILABLE_OPERATORS = ['+', '-', '*', '/']

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not possible")
        return None
    result = a / b
    return result

def main ()
    while True:
        # Getting the input expression from the user
        expression = input("Enter a mathematical expression (example: 5 - 3): ")
        if not expression:
            print("Error: empty input")  
            continue                       
        # Split the string into parts by spaces
        parts = expression.split()
        
        # Checking the input format
        if len(parts) != 3:
            print("Error: Incorrect input format")
            continue
        
        # Checking whether the operands are numbers
        try:
            a = float(parts[0])
            b = float(parts[2])
        except ValueError:
            print("Error: the operands must be numeric or float")
            continue
        
        # Checking the operand
        operator = parts[1]
        if operator not in AVAILABLE_OPERATORS:
            print(f"Error: unsupported operator '{operator}'. Available operators: {AVAILABLE_OPERATORS}")
            continue
        
    # Select the appropriate function to calculate
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        
        # Output of the result if it is not None
        if result is not None:
            print(result)
            return
        else:
            continue
    

# Start the program
if __name__ == "__main__":  
    main()
