'''
Example 21: Program to find the maximum, minimum and mean value from the inputted list

'''

# Prompt the user to enter a list of numbers
nums = input("Enter a list of numbers separated by spaces: ").split()

# Convert the list of strings to a list of floats
nums = [float(num) for num in nums]

# Find the maximum, minimum, and mean of the numbers
max_num = max(nums)
min_num = min(nums)
mean_num = sum(nums) / len(nums)

# Print the results
print("Maximum value:", max_num)
print("Minimum value:", min_num)
print("Mean value:", mean_num)
