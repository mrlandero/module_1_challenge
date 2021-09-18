
# List of loan costs stored into variable (loan_costs)
loan_costs = [500, 600, 200, 1000, 450]

# How many total loans in the list --> Using the len() function
number_of_loans = len(loan_costs)
print(f"There are a total of {number_of_loans} loans.")

# Total $ amount of loans in the list --> Using the sum() function
total_loan_amount = sum(loan_costs)
print(f"The total cost of the loans is ${total_loan_amount}")

# Average loan price --> total_loan_amount / number_of_loans
average_loan_price = total_loan_amount / number_of_loans
print(f"The average price per loan is ${average_loan_price}")

# Dictionary of Loan Information needing extraction with get()
loan_data = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extracting the value from the future_value key in order to store and use in calculations
future_value = loan_data.get("future_value")

# Extracting the value from the remining_months key in order to store and use in calculations
remaining_months = loan_data.get("remaining_months")

# Calculate and store the present_value of the loan
present_value = future_value / ((1 + 0.2) ** remaining_months)

# Print the present "fair" value of the loan
print(f"The fair value for this loan is: ${present_value: .2f}")

# Use get() to extract the loan_price and store to the variable loan_price
loan_price = loan_data.get("loan_price")

# Conditional statement to decide if the loan is worth the purchase price
# If the present value is greater than loan price, you should buy
if present_value > loan_price:
  print("This loan is a great value! You should BUY!")
# If the present value is the same as the loan price, proceed with caution
elif present_value == loan_price:
  print("The loan is valued right on target. Proceed with caution!")
# If the present value is less than the loan price, we should not buy
elif present_value < loan_price:
  print("This loan is poorly valued. DO NOT BUY!")
# In case something goes wrong or there is no loan price data, an error message
else:
  print("Not enough data is known to make a recommendation. Sorry!")

# We are given a new loan to calculate and determine if a good buy or not
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Create a variable to store the new loan's future value data
future_value_two = new_loan.get("future_value")

# Create a variable to store the new loan's remaining months data
remaining_months_two = new_loan.get("remaining_months")

# Define a the function calculate present value to be able to apply this code any time we need it
# The function includes the parameters (future value 2, remaining months 2 , annual rate)
def calculate_present_value(future_value_two, remaining_months_two, annual_discount_rate):
  # Store the present value result into a variable called present value 2
  present_value_two = future_value_two / ((1 + annual_discount_rate) ** remaining_months_two)
  # Return the value of present value two to the function to be called when needed
  return present_value_two

# Store the result from running the function into a variable called present value two
present_value_two = calculate_present_value(future_value_two, remaining_months_two, 0.2)
# Use formatted string to print out the fair value of the loan to 2 decimal places
print(f"The fair value of this loan is: ${present_value_two: .2f}")

# List of loans given to filter through and find the inexpensive ones, stored in a variable
loan_data_three = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list that we can later populate with inexpensive loans
inexpensive_loans = []

# Create the for loop to iterate through the list of dictionaries
for item in loan_data_three:
  # Retrieve the loan price info by targeting the loan prices from the list
   loan_price = item["loan_price"]
   # Print loan price to verify it grabbed the right numbers
   print(loan_price)
  # Create a conditional to test whether a certain loan price is under our $500 limit
   if loan_price <= 500:
     # If so, append the laon price to the list called inexpensive loans using the append() method
     inexpensive_loans.append(loan_price)

# Print the resulting new list in a formatted string
print(f"The new list of inexpensive loans is: {inexpensive_loans}")
  
  

  

  






