# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    return read_portfolio_dict(filename)


def read_portfolio_tuples(filename):
    '''opens a given portfolio file and reads it into a list of tuples'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio

def read_portfolio_dict(filename):
    '''opens a given portfolio file and reads it into a list of dicts'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            portfolio.append({ 'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price'])})
    return portfolio

def read_prices(filename):
    prices = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            print("index error, skipping line")
    f.close()
    return prices

def gain_loss(portfolio, prices):
    current_value = 0.0
    prior_value = 0.0
    for holding in portfolio:
        prior_value += holding['shares'] * holding['price']
        current_value += holding['shares'] * prices[holding["name"]]
    print("current Value is", current_value, "prior value is", prior_value, "the gain/loss is", current_value - prior_value)

def report_data(portfolio,prices):
    report = []
    for holding in portfolio:
        current_price = prices[holding['name']]
        name, shares, change = holding['name'], holding['shares'], holding['price'] - current_price
        report.append((name, shares, current_price, change))
    return report

def print_report(report_data):
    print('%10s %10s %10s %10s' % ('Name', 'Shares', 'Price', 'Change'))
    print('---------- ---------- ---------- -----------')
    for r in report_data:
        print('%10s %10d %10.2f %10.2f' % r)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print_report(report_data(read_portfolio(filename),read_prices('Data/prices.csv')))