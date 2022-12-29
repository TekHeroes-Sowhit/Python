
import requests
import matplotlib.pyplot as plt
api_key=open('api_key','r').read()
company="FB"
years=2
balance_sheet=request.get(f'https://financialmodelig')
balancesheet=balance_sheet.json()
## Total current assets
total_current_assets=balancesheet[0]['totalCurrentAssets']
total_current_lia=balancesheet[1]['totalCurrentLiabilites']
print(f'the total current assies of {company} is {total_current_assets}')
print(f'the total current assies of {company} is {total_current_lia}')
total_debt=balancesheet[0]['debt']
cash_and_equivalence=balancesheet[0]['cashAndCashEquivalence']
cash_debt_diff=cash_and_equivalence-total_debt
print(f' the cash_debt is {cash_debt::,.%2f}')
# print(balancesheet[0].keys())

