for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*", end='')
print()

number_of_star_rows = number_of_stars
for current_star_row_number in range(1, number_of_star_rows + 1):
    for i in range(1, current_star_row_number + 1):
        print("*", end='')
    print("")


