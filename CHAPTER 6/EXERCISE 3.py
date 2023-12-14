# Formulas
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplnum2(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

def modulus(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Cannot calculate modulus with zero divisor."

def check_greater(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}."
    elif num1 < num2:
        return f"{num2} is greater than {num1}."
    else:
        return "Both numbers are equal."

# Disply the calculator menu
def calculator_menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")

# Enter the choice for calculator menu
calculator_menu()
choice = input("Enter your choice (1-6): ")

# Enter 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the arithmetic operation
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} =", result)
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} =", result)
elif choice == '3':
    result = multiplnum2(num1, num2)
    print(f"{num1} * {num2} =", result)
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} =", result)
elif choice == '5':
    result = modulus(num1, num2)
    print(f"{num1} % {num2} =", result)
elif choice == '6':
    result = check_greater(num1, num2)
    print(result)
else:
    print("Invalid input. Please enter a number between 1 and 6.")
