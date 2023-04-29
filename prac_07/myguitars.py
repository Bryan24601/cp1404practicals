import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        return self.year < other.year


guitar_file = open('guitars.csv', 'r')
guitar_list = []

guitar_file.readline()
for line in guitar_file:
    parts = line.strip().split(',')
    current_guitar = Guitar(parts[0], parts[1], parts[2])
    guitar_list.append(current_guitar)
sorted_guitar_list = sorted(guitar_list)
for guitar in sorted_guitar_list:
    print(guitar)
