'''

Example 18: Consider two strings:

strl = "Hello"

str2 = "Python"

Observe the result obtained after performing important string operations.

'''

# Define the two strings
str1 = "Hello"
str2 = "Python"

# Concatenate the two strings
concatenated_str = str1 + " " + str2
print("Concatenated string:", concatenated_str)

# Get the length of the two strings
len_str1 = len(str1)
len_str2 = len(str2)
print("Length of str1:", len_str1)
print("Length of str2:", len_str2)

# Accessing individual characters in a string using indexing
print("First character of str1:", str1[0])
print("Third character of str2:", str2[2])

# Slicing a string to get a substring
substring_str1 = str1[1:4]
print("Substring of str1:", substring_str1)

# Converting a string to uppercase or lowercase
uppercase_str2 = str2.upper()
lowercase_str1 = str1.lower()
print("Uppercase str2:", uppercase_str2)
print("Lowercase str1:", lowercase_str1)

# Replacing a substring in a string
new_str1 = str1.replace("l", "p")
print("New str1:", new_str1)

# Splitting a string into a list of substrings
split_str2 = str2.split("t")
print("Split str2:", split_str2)




# Define the two strings
str1 = "Hello"
str2 = "Python"

# Check if a substring is present in a string
is_present = "llo" in str1
print("Is 'llo' present in str1?", is_present)

# Count the number of occurrences of a substring in a string
count_l_in_str1 = str1.count("l")
print("Number of occurrences of 'l' in str1:", count_l_in_str1)

# Check if a string starts or ends with a particular substring
starts_with_hello = str1.startswith("Hello")
ends_with_on = str2.endswith("on")
print("Does str1 start with 'Hello'?", starts_with_hello)
print("Does str2 end with 'on'?", ends_with_on)

# Join a list of strings into a single string using a delimiter
words = ["hello", "world", "python"]
joined_string = "-".join(words)
print("Joined string:", joined_string)

# Strip whitespace characters from the beginning and end of a string
str3 = "   Hello Python   "
stripped_str3 = str3.strip()
print("Stripped str3:", stripped_str3)

# Format a string using placeholders
age = 25
name = "John"
formatted_string = "My name is {0} and I am {1} years old".format(name, age)
print("Formatted string:", formatted_string)



