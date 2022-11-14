# report.py
#
# Exercise 2.4

import csv
import locale

def read_portfolio(filename):
    '''read portfolio positions from file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            values = (row[0], int(row[1]), float(row[2]))
            holding = dict(zip(headers,values))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''read stock prices from filename'''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                stock, price = row
                prices[stock] = float(price)
    return prices

def calculate_portfolio_value(portfolio, prices):
    portfolio_value = 0
    gain_loss = 0
    for position in portfolio:
        purchase_cost = position['shares'] * position['price']
        current_value = position['shares'] * prices[position['name']]
        portfolio_value += current_value
        gain_loss += current_value - purchase_cost
    return portfolio_value, gain_loss

def make_report(portfolio, prices):
    report = []
    for pos in portfolio:
        cur_price = prices[pos['name']]
        row = (pos['name'], pos['shares'], cur_price, cur_price - pos['price'])
        report.append(row)
    return report


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    prices    = read_prices('Data/prices.csv')

    # for Exercise 2.7
    # current_value, gain_loss = calculate_portfolio_value(portfolio, prices)
    # print(f'Total cost: {(current_value - gain_loss):,.2f}')
    # print(f'Current value: {current_value:,.2f}')
    # print(f'Gain/Loss: {gain_loss:,.2f}')

    locale.setlocale(locale.LC_MONETARY, 'en_us')
    report = make_report(portfolio, prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        # print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        dollar_price = locale.currency(price, symbol=True)
        print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')
