'''
Example 17: Program to calculate the total amount payable by the customer on purchase of any item with GST levied on it. Develop a user-friendly approach for the program using while loop.

'''


# take user input for the item price and GST percentage
price = float(input("Enter the item price: "))
gst_rate = float(input("Enter the GST rate (%): "))

# check if the GST rate is valid
while gst_rate < 0 or gst_rate > 100:
    print("Invalid GST rate entered. Please enter a value between 0 and 100.")
    gst_rate = float(input("Enter the GST rate (%): "))

# calculate the GST amount and total amount payable
gst_amt = price * gst_rate / 100
total_amt = price + gst_amt

# print the result
print(f"Item price: Rs. {price:.2f}")
print(f"GST rate: {gst_rate:.2f}%")
print(f"GST amount: Rs. {gst_amt:.2f}")
print(f"Total amount payable: Rs. {total_amt:.2f}")
