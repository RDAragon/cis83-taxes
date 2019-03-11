'''
NAME: main.py
AUTHOR: Roger Aragon
DATE: 3/10/19
EMAIL: aragonr87056@student.vvc.edu
DESCRIPTION: calculates income tax based on income
'''

income = int(input('Enter annual income: '))

if income > 500000:
    tax = (income * 0.01) + (income * 0.06)
elif income > 250000:
    tax = (income * 0.01) + (income * 0.05)
elif income > 100000:
    tax = (income * 0.01) + (income * 0.04)
elif income > 75000:
    tax = (income * 0.01) + (income * 0.03)
elif income > 50000:
    tax = (income * 0.01) + (income * 0.02)
elif income <= 50000:
    tax = (income * 0.01)

print ('Your income tax for your income of $%d is: $%d.' %(income, tax))
 
