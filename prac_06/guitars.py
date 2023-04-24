from prac_06.guitar import Guitar

guitar_list = []
print("My Guitars!")
current_guitar_name = input("Name: ")
while current_guitar_name != "":
    current_guitar_year = input("Year: ")
    current_guitar_cost = input("Cost: $")
    current_guitar = Guitar(current_guitar_name, current_guitar_year, current_guitar_cost)
    guitar_list.append(current_guitar)
    print(f"{current_guitar.name} ({current_guitar.year}): ${current_guitar.cost} added")
    current_guitar_name = input("Name: ")

print("These are my guitars:")
current_line_number = 0
for current_line in guitar_list:
    current_line_number += 1
    if current_line.is_vintage():
        vintage_status = "(Vintage)"
    else:
        vintage_status = ""
    print("Guitar {}: {:>20}, worth $ {:>10,.2f} {}").format(current_line_number, current_line.name, current_line.year, current_line.cost, vintage_status)