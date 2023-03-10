'''

Example 19: Consider a string str1 with the following content.

strl= "Hello Python"

The various slice operations and the output retrieved are shown below:

'''

# Define the string
str1 = "Hello Python"

# Extract a substring using a positive index
substr1 = str1[0:5]
print("Substring from index 0 to 4:", substr1)

# Extract a substring using a negative index
substr2 = str1[-6:-1]
print("Substring from index -6 to -2:", substr2)

# Extract every other character in the string
every_other_char = str1[::2]
print("Every other character:", every_other_char)

# Reverse the string
reversed_str1 = str1[::-1]
print("Reversed string:", reversed_str1)

# Define the string
str1 = "Hello, World!"

# Extract a substring starting at index 7 to the end of the string
substr1 = str1[7:]
print("Substring from index 7 to the end of the string:", substr1)

# Extract a substring starting at the beginning of the string to index 5 (exclusive)
substr2 = str1[:5]
print("Substring from the beginning to index 5:", substr2)

# Extract a substring starting at index 7 and ending at index 12 (exclusive)
substr3 = str1[7:12]
print("Substring from index 7 to index 11:", substr3)

# Extract a substring starting at index 7 and ending at the end of the string, but only taking every other character
substr4 = str1[7::2]
print("Every other character from index 7 to the end of the string:", substr4)
