'''
Problem Statement:

Example 2: Lokesh has taken a loan of rupees 40000 from Vinod at the rate of 8% per annum, After 6 years, he wants to repay the loan in full including interest. Write the Python code fin script mode) to calculate and display the interest and total amount to be paid by Lokesh to settle his accounts.
'''

# Solution 

# Input
principal = 40000
rate = 0.08
time = 6

# Calculation
interest = principal * rate * time
total_amount = principal + interest

# Output
print("Interest to be paid: Rs.", interest)
print("Total amount to be paid: Rs.", total_amount)
