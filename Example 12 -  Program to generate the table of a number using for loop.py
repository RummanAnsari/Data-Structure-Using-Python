'''
Example 12: Program to generate the table of a number using for loop.
'''

# take user input for the number
num = int(input("Enter a number: "))

# use a for loop to generate the table
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
