import csv
from collections import Counter
wimbledon_file = open("wimbledon.csv", "r", encoding="utf-8-sig")
reader = csv.reader(wimbledon_file)
CHAMPION_COUNTS = {}
country_winners = []
country_winners_count = 0

next(reader)
for current_line in reader:
    if current_line[1] not in country_winners:  # Add to country_winners list if win
        country_winners.append(current_line[1])
        country_winners_count += 1

    if current_line[2] not in CHAMPION_COUNTS:  # Count Champion Wins
        CHAMPION_COUNTS[current_line[2]] = 0
    CHAMPION_COUNTS[current_line[2]] += 1

print("Wimbledon Champions:")
for current_line in CHAMPION_COUNTS:
    champion_name, number_of_wins = current_line, CHAMPION_COUNTS[current_line]
    print(f"{champion_name} {number_of_wins}")

print(f"These {country_winners_count} countries have won Wimbledon:")
print(','.join(sorted(country_winners)))