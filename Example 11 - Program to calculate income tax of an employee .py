'''
Example 11: Program to calculate income tax of an employee on the basis of basic salary and total savings inputted by the user (using nested if...else statement) as per the given slabs:

--> No tax for individuals with income less than 2.5 lakh

--> 0%-5% tax with income 2.5 lakh to 5 lakh for different age groups

--> 20% tax with income 5 lakh to 10 lakh

--> Investments up to 1.5 lakh under Sec 80C can save up to 45,000 in taxes.

'''


# Taking input from the user
basic_salary = float(input("Enter your basic salary: "))
total_savings = float(input("Enter your total savings under Sec 80C: "))

# Calculating taxable income
taxable_income = basic_salary - total_savings

# Calculating income tax based on the taxable income
if taxable_income < 250000:
    tax = 0
elif taxable_income < 500000:
    age = int(input("Enter your age: "))
    if age < 60:
        tax = (taxable_income - 250000) * 0.05
    elif age < 80:
        tax = (taxable_income - 250000) * 0.03
    else:
        tax = (taxable_income - 250000) * 0.0
elif taxable_income < 1000000:
    tax = (taxable_income - 500000) * 0.2
else:
    tax = (taxable_income - 1000000) * 0.3

# Deducting tax saving under Sec 80C
if total_savings <= 150000:
    tax = tax
elif total_savings > 150000 and total_savings <= 300000:
    tax = tax - ((total_savings - 150000) * 0.05)
elif total_savings > 300000 and total_savings <= 500000:
    tax = tax - (7500 + (total_savings - 300000) * 0.1)
else:
    tax = tax - (32500 + (total_savings - 500000) * 0.15)

# Displaying the income tax
print("Your income tax is:", tax)
