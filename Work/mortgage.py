# mortgage.py
#
# Exercise 1.7
principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000
month = 0

while principal > 0:
    month += 1
    this_payment = payment
    
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        this_payment += extra_payment
        
    if principal * (1+rate/12) < this_payment:
        this_payment = principal * (1+rate/12)
        
    principal = principal * (1+rate/12) - this_payment
        
    total_paid = total_paid + this_payment
    print(f'{month:>3.0f} {round(total_paid,2):10.2f} {round(principal,2):10.2f}')
    
    
print(f'Total paid: {round(total_paid,2):14.2f}')
print(f'Months: {month:18.0f}')
