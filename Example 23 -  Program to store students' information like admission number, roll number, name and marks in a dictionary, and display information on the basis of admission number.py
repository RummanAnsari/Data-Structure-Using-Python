'''
Example 23: Program to store students' information like admission number, roll number, name and marks in a dictionary, and display information on the basis of admission number.

'''

# Initialize an empty dictionary to store student information
students = {}

# Prompt the user to enter information for each student
while True:
    admission_num = input("Enter admission number (or 'done' to finish): ")
    if admission_num == 'done':
        break
    roll_num = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    students[admission_num] = {'roll_num': roll_num, 'name': name, 'marks': marks}

# Prompt the user to enter an admission number to search for
search_num = input("Enter admission number to search for: ")

# Print the student information for the admission number
if search_num in students:
    info = students[search_num]
    print("Roll number:", info['roll_num'])
    print("Name:", info['name'])
    print("Marks:", info['marks'])
else:
    print("Admission number not found.")
