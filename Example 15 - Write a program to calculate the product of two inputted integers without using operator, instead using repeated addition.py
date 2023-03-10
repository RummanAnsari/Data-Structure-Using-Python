'''
Example 15: Write a program to calculate the product of two inputted integers without using operator, instead using repeated addition.
'''

# take user input for the two integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# initialize the product to 0
product = 0

# use a for loop to perform repeated addition
for i in range(num2):
    product += num1

# print the result
print(f"The product of {num1} and {num2} is {product}")
