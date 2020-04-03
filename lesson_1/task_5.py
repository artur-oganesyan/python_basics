proceeds = int(input('Enter proceeds: '))
costs = int(input('Enter costs: '))
if proceeds > costs:
    print('You have a profit')
    profit = proceeds - costs
    profitability = profit / proceeds * 100
    print(f'Your profitability {profitability:.2f} %')
    firm_size = int(input("Enter firm size: "))
    profit_for_one_employee = profit / firm_size
    print(f'Profit for one employee is {profit_for_one_employee:.2f}')
elif proceeds == costs:
    print('You have no profit')
else:
    print('You are incurring losses')
