def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Exponentiation (**)")
    print("7. Modulus (%)")

    # Get user input
    choice = input("Enter the number of the operation (1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            # Get two numbers from the user
            X = float(input("Enter the first number: "))
            Y = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == '1':
                print(f"The result is: {X + Y}")
            elif choice == '2':
                print(f"The result is: {X - Y}")
            elif choice == '3':
                print(f"The result is: {X * Y}")
            elif choice == '4':
                if Y != 0:
                    print(f"The result is: {X / Y}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"The result is: {X // Y}")
            elif choice == '6':
                   print(f"The result is: {X ** Y}")
            elif choice == '7':
                print(f"The result is: {X % Y}")
        except ValueError:
            print("Error: Please enter valid numbers.")
    else:
        print("Invalid choice. Please restart and select a valid operation.")

# Run the calculator
calculator()
