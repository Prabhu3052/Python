def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        try:
            choice = input("\nEnter choice (1-4), or 'q' to quit: ")
            
            if choice.lower() == 'q':
                print("Thank you for using the calculator!")
                break
                
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please enter a number between 1-4")
                continue
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"\n{num1} + {num2} = {result}")
            
            elif choice == '2':
                result = num1 - num2
                print(f"\n{num1} - {num2} = {result}")
            
            elif choice == '3':
                result = num1 * num2
                print(f"\n{num1} * {num2} = {result}")
            
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print(f"\n{num1} / {num2} = {result}")
                    
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()