'''
Example 9: Program to calculate and display the difference of two inputted numbers.

'''
# Way 1: Without Checking which number is bigger

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculating the difference
difference = num1 - num2

# Displaying the result
print("The difference of", num1, "and", num2, "is", difference)


# Way 2: Checking which number is bigger

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Checking which number is bigger
if num1 > num2:
    difference = num1 - num2
else:
    difference = num2 - num1

# Displaying the result
print("The difference of", num1, "and", num2, "is", difference)
