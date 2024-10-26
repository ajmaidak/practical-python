# pcost.py
#
# Exercise 1.27
#
# opens portfolio.csv, reads all the lines and calculates how much it
# cost to purchase all the shares
# expected output:
# Total cost 44671.15
total_cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for l in f:
        name, shares, price = l.split(',')
        total_cost += int(shares) * float(price)
print("Total cost", total_cost)

