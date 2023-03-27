import random


def main():
    total_years_simulated = 10
    welcome = "Welcome to the Gopher Population Simulator!"
    starting_population = 1000
    print(welcome)
    print(f"Starting population: {starting_population}")
    print("Year 1")
    current_population = starting_population
    for current_year in range(2, total_years_simulated + 1):
        current_population_growth = population_growth(current_population) // 1
        current_population_decline = population_decline(current_population) // 1
        current_population += current_population_growth
        current_population -= current_population_decline
        print(f"{current_population_growth} gophers were born. {current_population_decline} died.")
        print(f"Population: {current_population}")
        print(f"Year {current_year}\n")


def population_growth(current_population):
    growth_lower_percentage = 10
    growth_higher_percentage = 20
    current_growth_percentage = random.randint(growth_lower_percentage, growth_higher_percentage + 1) / 100
    current_growth = current_growth_percentage * current_population
    return current_growth


def population_decline(current_population):
    decline_lower_percentage = 5
    decline_higher_percentage = 25
    current_decline_percentage = random.randint(decline_lower_percentage, decline_higher_percentage + 1) / 100
    current_decline = current_decline_percentage * current_population
    return current_decline


main()
