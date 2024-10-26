# pcost.py
#
# Exercise 1.30
#
# opens portfolio.csv, reads all the lines and calculates how much it
# cost to purchase all the shares
# expected output:
# Total cost 44671.15

import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    for r in rows:
        name, shares, price = r
        try:
            total_cost += int(shares) * float(price)
        except ValueError:
            print("couldn't parse line:", r, "skipping")

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
