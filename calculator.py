def calculator():
    print("Welcome to the simple calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on user input
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please select 1, 2, 3, or 4.")

# Run the calculator function
calculator()
