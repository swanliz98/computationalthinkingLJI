#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:28:25 2019

@author: swanliz98
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
minimummospayment = 1 #need to figure out how to calculate this!
if monthly_payment >= minimummospayment:
    print("The monthly payment of $" + monthly_payment + " will work!")
else:
    print("The monthly payment of $" + monthly_payment + "will not work. You would be paying off this loan forever!")

print("The minimum monthly payment for this loan would be " + minimummospayment + "dollars.")


'''
Part C - Determine how long it will take to pay off your student loans
'''

months = 0

while total_owed <= 0:
    months +=1
    total_owed -= monthly_payment
    # add back interest accrued that month

yearstopay = months/12
print("With a monthly payment of", monthly_payment, ", it will take", months, "months to pay off your student loans.")
print("Or", yearstopay, "years to pay off your student loans.")


