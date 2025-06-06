def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    
    elif operation == "subtract":
        return num1 - num2
    
    elif operation == "multiply":
        return num1 * num2
    
    elif operation == "divide":
        if num2 == 0:
            return "Error! number cannot divide 0." #Used return instead of print because after print, the program still returns a None.
        else:
            return num1 / num2
    else:
        return "Invalid Operation!"
    
"""Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

Requirements for arithmetic_operations.py:
Function Definition:
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
Return the result of the arithmetic operation.

Note: - Focus on implementing the perform_operation function in arithmetic_operations.py. Ensure your function correctly handles the operations based on the inputs. - You do not need to create or modify main.py. It is provided for you to test your function. The checker will use this main.py to import your arithmetic_operations.py script and test its functionality.

"""

"""from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()"""