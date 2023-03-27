import random
temperature_write_file = open("temps_input", "a")
number_of_temperatures = 15
for current_temperature in range(1, number_of_temperatures + 1):
    new_temperature = random.randint(-200, 201)
    print(new_temperature)
    temperature_write_file.write(f"{new_temperature}\n")
