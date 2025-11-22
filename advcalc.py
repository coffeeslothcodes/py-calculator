import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(x)

def sin_val(x):
    return math.sin(x)

def cos_val(x):
    return math.cos(x)

def tan_val(x):
    return math.tan(x)

def log_val(x):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive numbers."
    return math.log(x)

def calculator():
    print("--- Simple CLI Calculator ---")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (x + y)")
        print("2. Subtract (x - y)")
        print("3. Multiply (x * y)")
        print("4. Divide (x / y)")
        print("5. Power (x ^ y)")
        print("6. Square Root (√x)")
        print("7. Sine (sin(x))")
        print("8. Cosine (cos(x))")
        print("9. Tangent (tan(x))")
        print("10. Natural Logarithm (ln(x))")
        print("11. Exit")

        choice = input("Enter choice (1-11): ")

        if choice == '11':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            
            print(f"\nResult: {result}")

        elif choice in ('6', '7', '8', '9', '10'):
            try:
                num1 = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '6':
                result = square_root(num1)
            elif choice == '7':
                result = sin_val(num1)
            elif choice == '8':
                result = cos_val(num1)
            elif choice == '9':
                result = tan_val(num1)
            elif choice == '10':
                result = log_val(num1)
            
            print(f"\nResult: {result}")
            
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

calculator()
