def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_number = int(input("How many months? "))
    # month_number store number of months

    for month_number in range(1, month_number + 1):
        # income = float(input("Enter income for month " + str(month_number) + ": "))
        income = float(input(f"Enter income for month {month_number}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month_number in range(1, month_number + 1):
        income = incomes[month_number - 1]
        total += income
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
        print(f"Month {month_number} - Income: ${income} Total: ${total}")


main()