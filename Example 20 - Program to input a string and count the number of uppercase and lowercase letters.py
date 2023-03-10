'''
Example 20: Program to input a string and count the number of uppercase and lowercase letters

'''

# Prompt the user to enter a string
string = input("Enter a string: ")

# Initialize counters for uppercase and lowercase letters
num_uppercase = 0
num_lowercase = 0

# Loop over each character in the string
for char in string:
    # Check if the character is uppercase
    if char.isupper():
        num_uppercase += 1
    # Check if the character is lowercase
    elif char.islower():
        num_lowercase += 1

# Print the results
print("Number of uppercase letters:", num_uppercase)
print("Number of lowercase letters:", num_lowercase)
