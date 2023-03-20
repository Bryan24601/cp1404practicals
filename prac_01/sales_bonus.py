"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
base_commission_rate = 10
high_commission_rate = 15
sales = float(input("Enter sales: $"))
while sales >= 0:
    commission = sales * base_commission_rate
    if sales >= 1000:
        commission = sales * high_commission_rate
    print(f"Your commission is ${commission:2f}.")
    sales = float(input("Enter sales: $"))
else:
    print("Invalid Input")