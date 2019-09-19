#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Edited on Wed Sep 18 2019 by iperrilles

@author: Isaac Perrilles, Jessica Tse, Liz Swanson
"""

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
print("Total amount owed at graduation:", total_owed)

'''
Part B - Determine if monthly payment is feasible
'''

monthly_payment = float(input("Enter a monthly payment goal "))
monthly_interest = float((interest_rate/12)*total_owed)

if monthly_payment < monthly_interest:
    print(f"A monthly payment of {monthly_payment} won't work! You'll be paying off your loans forever.")
	else: 
    print(f"A monthly payment of {monthly_payment} will work!")
	
print("The minimum monthly payment for this loan would be " + monthly_interest + "dollars.")

'''
Part C - Determine how long it will take to pay off your student loans
'''

months = 0
while total_owed > 0:
    months += 1
    total_owed -= monthly_payment
	total_owed = total_owed*(1 + interest_rate/12)

yearstopay = months/12
print("With a monthly payment of", monthly_payment, ", it will take", months, "months to pay off your student loans.")
print("Or", yearstopay, "years to pay off your student loans.")


