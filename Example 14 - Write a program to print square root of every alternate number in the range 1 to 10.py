'''
Example 14: Write a program to print square root of every alternate number in the range 1 to 10.
'''

import math

# use a for loop to iterate over every alternate number in the range 1 to 10
for num in range(1, 11, 2):
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")
