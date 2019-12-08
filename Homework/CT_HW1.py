'''
Part A - Calculating total amount owed after graduation
'''
loan_per_year = float(input("Enter the loan amount per year: "))
interest_rate = float(input("Enter the loan interest rate: "))
years = int(input("Enter the number of years you will be taking a loan: "))
total_owed = 0
counter = 0

while counter < years:
    total_owed = (loan_per_year + total_owed)*(1+ interest_rate)
    counter += 1
print(f"Total amount owed at graduation: ${total_owed:0.2f}")

'''
Part B - Determine if monthly payment is feasible
'''

monthly_payment = float(input("Enter a monthly payment goal: "))
monthly_interest = float((interest_rate/12)*total_owed)

if monthly_payment < monthly_interest: 
    print(f"A monthly payment of ${monthly_payment:0.2f} won't work! You'll be paying off your loans forever.")
else: 
    print(f"A monthly payment of ${monthly_payment:0.2f} will work!")	
print(f"The minimum monthly payment for this loan would be ${monthly_interest:0.2f}.")


'''
Part C - Determine how long it will take to pay off your student loans
'''

months = 0
while total_owed > 0:
    months += 1
    total_owed -= monthly_payment
    total_owed = total_owed * (1 + (interest_rate/12))

yearstopay = months/12

print(f"With a monthly payment of ${monthly_payment:0.2f}, it will take {months} months to pay off your student loans.")
print(f"Or {yearstopay:0.2f} years to pay off your student loans.")

