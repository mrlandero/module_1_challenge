
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

