'''
Example 10: Program to illustrate nested if...else through a four-function calculator.
'''

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Performing the calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Handling division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator")

# Displaying the result
if operator == '/' and num2 == 0:
    pass  # Do nothing
else:
    print(num1, operator, num2, "=", result)
