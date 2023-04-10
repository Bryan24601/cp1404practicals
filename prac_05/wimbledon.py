import csv
from collections import Counter
wimbledon_file = open("wimbledon.csv", "r", encoding="utf-8-sig")
reader = csv.reader(wimbledon_file)

print("Wimbledon Champions:\n")
next(reader)
champion_counts = Counter(current_row[3] for current_row in reader)
print(champion_counts)

# Fake change