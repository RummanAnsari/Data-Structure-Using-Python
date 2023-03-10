'''
Example 16: Program to calculate factorial of a number using while loop.

'''

# take user input for the number
num = int(input("Enter a number: "))

# initialize variables
fact = 1
i = 1

# use a while loop to calculate the factorial
while i <= num:
    fact *= i
    i += 1

# print the result
print(f"The factorial of {num} is {fact}")
