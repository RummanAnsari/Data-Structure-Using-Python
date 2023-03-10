'''
Example 6: Write a Python code to calculate simple interest and amount payable by inputting the value of principal amount and rate from the user for a time period of 5 years.

(Formula used: Simple Interest = Principal * Rate * Time/100)
'''

# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))

# Time period is fixed at 5 years
time = 5

# Calculating simple interest and amount payable
simple_interest = (principal * rate * time) / 100
amount_payable = principal + simple_interest

# Displaying the result
print("Simple Interest = ", simple_interest)
print("Amount Payable = ", amount_payable)


# Output

# Enter the principal amount: 10000
# Enter the rate of interest: 2
# Simple Interest =  1000.0
# Amount Payable =  11000.0