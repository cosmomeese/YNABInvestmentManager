import ynab



path = 'D:\Dropbox\YNAB'
budgetName = 'Budget'

from ynab import YNAB

ynab = YNAB(path,budgetName)

print(ynab.accounts)