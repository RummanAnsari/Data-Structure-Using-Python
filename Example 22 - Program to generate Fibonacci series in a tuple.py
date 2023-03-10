'''
Example 22: Program to generate Fibonacci series in a tuple.

'''


# Prompt the user to enter the number of terms in the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate the Fibonacci series
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])

# Convert the list to a tuple
fib = tuple(fib)

# Print the results
print("Fibonacci series:", fib)
