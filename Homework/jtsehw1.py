# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:16:16 2019

@author: Jessica Tse
"""
#Part A
loan_per_year = int(input("Input loan per year: "))
interest_rate = float(input("Input interest rate: "))
years = int(input("Input years: "))
total_owed = 0
counter = 0
while counter < years: 
    total_owed = (loan_per_year + total_owed)*(1 + interest_rate)
    counter += 1
print(f"Total amount owed is {total_owed}")

#Part B
monthly_payment = int(input("Input monthly payment: "))
monthly_interest = int((interest_rate/12)*total_owed)
if monthly_payment < (interest_rate/12)*total_owed:
    print(f"not possible to pay off; need at least ${monthly_interest} to pay off!")
else: 
    print(f"possible to pay off! minimum payment required is ${monthly_interest}")

month_count = 0
while total_owed > 0:
    total_owed = total_owed - monthly_payment
    total_owed = total_owed*(1 + interest_rate/12)
    month_count += 1
print(f"It will take {month_count} months to pay off your student loans if you pay ${monthly_payment}.")
print(f"It will take {round(month_count/12,2)} years to pay off your student loans." )
