# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        header = next(f).strip().split(',')
        for raw_line in f:
            line = raw_line.strip()
            _, num_shares_str, price_str = line.split(',')
            try:
                num_shares = int(num_shares_str)
                price = float(price_str)
            except ValueError:
                print(f'Unable to parse line {line}')
            total_cost += (num_shares * price)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost {cost:,.2f}')

