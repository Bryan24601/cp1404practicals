number_of_items = int(input("Number of items: "))
total_cost = 0
original_percentage_cost = 100
while number_of_items < 0:
    print("INvalid number of items!")
    number_of_items = int(input("Number of items: "))

for current_item in range(1, number_of_items + 1):
    current_item_price = float(input("Price of item: "))
    total_cost += current_item_price

if total_cost > 100:
    discounted_percentage = original_percentage_cost - 10

final_cost = total_cost * discounted_percentage / original_percentage_cost
print(f"Total price for {number_of_items} items is ${final_cost}")